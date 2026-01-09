import SmartDevice


class SecurityCamera(SmartDevice):
    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
        resolution: str,
        night_vision: bool
    ):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        return 50

    def connection_quality(self) -> int:
        return 9

    def info(self) -> dict[str, float | int | str]:
        data = super().info()
        data["resolution"] = self.resolution
        data["night_vision"] = self.night_vision
        return data
