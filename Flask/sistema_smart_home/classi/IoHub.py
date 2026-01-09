import SmartDevice


class IoTHub:
    def __init__(self):
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> SmartDevice | None:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_device: SmartDevice) -> None:
        if serial_number in self.devices:
            self.devices[serial_number].status = new_device.status

    def delete(self, serial_number: str) -> bool:
        if serial_number in self.devices:
            del self.devices[serial_number]
            return True
        return False

    def list_all(self) -> list[dict[str, float | int | str]]:
        return [device.info() for device in self.devices.values()]
