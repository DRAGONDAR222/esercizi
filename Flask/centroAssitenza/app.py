from classi import ServiceCenter
from classi import Laptop
from classi import Smartphone
import StatusEnum
from flask import Flask, request, url_for, jsonify

app = Flask(__name__)

# Creazione del centro di assistenza
center = ServiceCenter()

# Creazione di un laptop
laptop1 = Laptop(
    id="L001",
    model="XPS 15",
    customer_name="Mario Rossi",
    purchase_year=2022,
    status=StatusEnum.RICEVUTO,
    has_dedicated_gpu=True,
    screen_size_inches=15.6
)

# Creazione di uno smartphone
smartphone1 = Smartphone(
    id="S001",
    model="iPhone 14",
    customer_name="Luca Bianchi",
    purchase_year=2023,
    status=StatusEnum.RICEVUTO,
    has_protective_case=True,
    storage_gb=256
)

# Aggiunta dei dispositivi al centro
center.add(laptop1)
center.add(smartphone1)

# -------------------- ROUTE home --------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Service Center API",
        "links": {
            "list_devices": "/devices",
            "sample_device": "/devices/d1",
            "sample_estimate":"/devices/d1/estimate/1.5"
        }
    })

# -------------------- ROUTE  GET --------------------

@app.get("/devices")
def list_devices():
    return jsonify(center.list_all()),200

@app.get("/devices/<device_id>")
def info(device_id):
    device = center.get(device_id)
    if not device:
        return jsonify({"error":"device not found"}), 404
    return jsonify(device.info()),200

@app.get("/devices/<device_id>/estimate/<factor>")
def device_factor(device_id,factor = 1.0):
        device = center[device_id]
        if not device:
            return jsonify({"error":"device not found"}), 404
        return jsonify({ 
            "id": device_id,
            "device_type": device.device_type(),
            "factor": factor,
            "estimated_total_minutes": device.estitated_total_time()
        }), 200


# -------------------- ROUTE POST --------------------

@app.post("/devices")
def add_device():
    data = request.get_json()
        
    if "type" not in data:
        return jsonify({"error: Missing 'type' field"}), 400
    
    device_type = data["type"]

    if device_type != "smartphone" and device_type != "laptop":
        return jsonify({"error": "Invalid device type"}), 400

    required_fields = ["id","model", "customer_name", "purchase_year", "status"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
        
    device_id = data["id"]

    if center.get(device_id):
        return jsonify({"error": f"Device with ID {device_id} already exists"}), 400

    if device_type == "smartphone":
        smartphone_fields = ["has_protective_case", "storage_gb"]
        for field in smartphone_fields:
            if field not in data:
                return jsonify({"error": f"Missing field for smartphone: {field}"}), 400
    
        device = Smartphone(
            data["id"],
            data["model"],
            data["customer_name"],
            data["purchase_year"],
            data["status"],
            data["has_protective_case"],
            data["storage_gb"]
        )

    else:
        laptop_fields = ["has_dedicated_gpu","screen_size_inches"]
        for field in laptop_fields:
            if field not in data:
                return jsonify({"error": f"Missing field for laptop: {field}"}), 400
            
        device = Laptop(
            data["id"],
            data["model"],
            data["customer_name"],
            data["purchase_year"],
            data["status"],
            data["has_dedicated_gpu"],
            data["screen_size_inches"]
        )

    center.add(device)

    return jsonify({
        "status": "ok",
        "info": device.info()
    }), 201
    
# -------------------- ROUTE  PUT --------------------

@app.put("/devices/<device_id>")
def change_device(device_id):

    device = center.get(device_id)
    if not device:
         return jsonify({"error": "device not found"}), 404
    else:
        data = request.get_json()

        device.model = data["model"]
        device.customer_name = data["customer_name"]
        device.purchase_year = data["purchase_year"]
        device.status = data["status"]

        # Campi specifici
        if isinstance(device, Smartphone):
                device.has_protective_case = data["has_protective_case"]
                device.storage_gb = data["storage_gb"]

        if isinstance(device, Laptop):
                device.has_dedicated_gpu = data["has_dedicated_gpu"]
                device.screen_size_inches = data["screen_size_inches"]

        return jsonify({
        "status": "updated",
        "info": device.info()
        }), 200
    
# -------------------- ROUTE  PATCH --------------------

@app.patch("/devices/<device_id>/status")
def modify_device(device_id):
     
    device = center.get(device_id)
    if not device:
        return jsonify({"error": "device not found"}), 404
    else:
        data = request.get_json()
        center.patch_status(device_id, data["status"])

        return jsonify({
        "status": "updated",
        "info": device.info()
        }), 200
    
# -------------------- ROUTE  DELETE --------------------

@app.delete("/devices/<device_id>")
def delete_device(device_id):
     
    device = center.get(device_id)
    if not device:
        return jsonify({"error": "device not found"}), 404
    else:
        center.remove(device_id)  

        return jsonify({"deleted": True, "id": device_id}), 200
