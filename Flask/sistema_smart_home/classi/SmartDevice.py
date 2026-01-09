from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str
    ):
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        pass

    @abstractmethod
    def energy_consumption(self) -> float | int:
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        pass

    def info(self) -> dict[str, float | int | str]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "device_type": self.device_type()
        }

    def diagnostics_time(self, factor: float = 1.0) -> float:
        return self.energy_consumption() * factor + self.connection_quality() * 10
