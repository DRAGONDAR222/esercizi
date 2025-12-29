import Device

class ServiceCenter():

    devices:dict

    def __init__(self):
        self.devices = {}


    def add(self,device:Device):
        if device.id in self.devices:
            return False
        self.devices[device.id] = device
        return True
    
    def get(self,device_id):
            return self.devices[device_id]
    
    def patch_status(self,device_id, new_status):
            self.devices[device_id].status = new_status

    def delete(self,device_id):
        if device_id in self.devices:
             self.devices.pop(device_id)
             return True
        return False
    
    def list_all(self):
        return [x.info() for x in self.devices.values()]
    
