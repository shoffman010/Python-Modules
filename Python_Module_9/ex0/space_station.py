from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

    def show(self) -> None:
        status = "Operational" if self.is_operational else "Not operational"
        print(
            "Space Station Data Validation",
            "========================================",
            "Valid station created:",
            f"ID: {self.station_id}",
            f"Name: {self.name}",
            f"Crew: {self.crew_size} people",
            f"Power: {self.power_level}%",
            f"Oxygen: {self.oxygen_level}%",
            f"Maintenance: {self.last_maintenance.date()}",
            f"Status: {status}",
            sep="\n",
        )


def main() -> None:
    # model_validate demonstrates Pydantic's conversion of numeric strings.
    station_data: dict[str, object] = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": "6",
        "power_level": "85.5",
        "oxygen_level": "92.3",
        "last_maintenance": datetime.now(),
    }
    station = SpaceStation.model_validate(station_data)
    station.show()

    print("\n========================================")
    try:
        SpaceStation(
            station_id="ISSFAIL",
            name="International Space Station",
            crew_size=22,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(str(error).split(" [type=", 1)[0])


if __name__ == "__main__":
    main()
