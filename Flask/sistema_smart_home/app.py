from classi import IoHub,SecurityCamera,SmartDevice,SmartBulb
from flask import Flask, request, url_for, jsonify

app = Flask(__name__)


hub = IoHub()

bulb = SmartBulb(
    "SN-101",
    "Philips",
    "Living Room",
    2023,
    "online",
    800,
    True
)

camera = SecurityCamera(
    "SN-202",
    "Nest",
    "Entrance",
    2022,
    "online",
    "1080p",
    True
)

hub.add(bulb)
hub.add(camera)


# -------------------- ROUTE home --------------------
@app.route("/")
def home():
    return jsonify({
    "message": "Smart Home Hub API",
    "links": {
        "vehicles_list": "/devices",
        "vehicle_sample": "/devices/SN-101",
        "estimate_sample": "/devices/SN-101/diagnostic/1.0"
    }
})

@app.get("/devices")
def list_devices():
    return jsonify(hub.list_all()),200

@app.get("/devices/<serial_number>")
def info(serial_number):
    device = hub.get(serial_number)
    if not device:
        return jsonify({"error":"device not found"}), 404
    return jsonify(device.info()),200

@app.get("/devices/<serial_number>/diagnostic/<factor>")
def diagnostics_time(serial_number, factor = 1.0):
    device = hub.get(serial_number)
    if not device:
        return jsonify({"error: device not found"}), 404
    return jsonify({
        "serial_number": device.serial_number,
        "device_type": device.device_type(),
        "factor" : factor,
        "diagnostics_seconds" : device.diagnostics_time(factor)
    }), 200

# -------------------- ROUTE POST --------------------

@app.post("/devices")
def add_deevice():
    data = request.get_json()

    if "type" not in data:
        return jsonify({"error: Missing 'type' field"}), 400
    
    device_type = data["type"]

    if device_type != "bulb" and device_type != "security_camera":
        return jsonify({"error": "Invalid device type"}), 400
    
    require_fileds = ["serial_number","brand","room","installation_year","status"]
    for field in require_fileds:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
        
    device_serial = data["serial_number"]

    if hub.get(device_serial):
        return jsonify({"error": f"Device with serial {device_serial} already exists"}), 400

    if device_type == "bulb":
        bulb_fields = ["brightness_lumens","color_capability"]
        for field in bulb_fields:
            if field not in data:
                return jsonify({"error": f"Missing field for bulb: {field}"}), 400
    
        device = SmartBulb(
            data["serial_number"],
            data["brand"],
            data["room"],
            data["installation_year"],
            data["status"],
            data["brightness_lumens"],
            data["color_capability"]
        )


    else:
        securityCamera_fields = ["resolution","night_vision"]
        for field in securityCamera_fields:
            if field not in data:
                return jsonify({"error": f"Missing field for securityCamera: {field}"}), 400
            

        device = SecurityCamera(
            data["serial_number"],
            data["brand"],
            data["room"],
            data["installation_year"],
            data["status"],
            data["resolution"],
            data["night_vision"]
        )

    hub.add(device)

    return jsonify({
        "status": "ok",
        "info": device.info()
    }), 201


# -------------------- ROUTE  PUT --------------------

@app.put("/devices/<serial_number>")
def change_device(serial_number):
    
    device = hub.get(serial_number)
    if not device:
        return jsonify({"error":"device not found"}), 404
    else:
        data = request.get_json()

        device.brand = data["brand"]
        device.room = data["room"]
        device.installation_year = data["installation_year"]
        device.status = data["status"]
        
        if isinstance(device, SmartBulb):
            device.brightness_lumens = data["brightness_lumens"]
            device.color_capability = data["color_capability"]

        if isinstance(device, SecurityCamera):
            device.resolution = data["resolution"]
            device.night_vision = data["night_vision"]

        return jsonify({
            "status": "updated",
            "info": device.info()
        }), 200
    
# -------------------- ROUTE  PATCH --------------------

@app.patch("/devices/<serial_number>/status")
def modify_device(serial_number):

    device = hub.get(serial_number)
    if not device:
        return jsonify({"error":"device not found"}), 404
    else:
        data = request.get_json()
        hub.patch_status(serial_number,data["status"])

        return jsonify({
        "status": "updated",
        "info": device.info()
        }), 200

# -------------------- ROUTE  DELETE --------------------

@app.delete("/devices/<serial_number>")
def delete_device(serial_number):

    device = hub.get(serial_number)
    if not device:
        return jsonify({"error": "device not found"}), 404
    else:
        hub.delete(serial_number)  

        return jsonify({"deleted": True, "id": serial_number}), 200



if __name__ == "__main__":
    app.run(debug=True)