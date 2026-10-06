from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_safety(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        ):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < total_crew / 2:
                raise ValueError(
                    "Long missions (>365 days) need at least 50% of crew "
                    "with 5+ years of experience"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self

    def show(self) -> None:
        print(
            "Valid mission created:",
            f"Mission: {self.mission_name}",
            f"ID: {self.mission_id}",
            f"Destination: {self.destination}",
            f"Duration: {self.duration_days} days",
            f"Budget: ${self.budget_millions}M",
            f"Crew size: {len(self.crew)}",
            "Crew members:",
            sep="\n",
        )
        for member in self.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )


def main() -> None:
    crew: list[CrewMember] = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=29,
            specialization="Engineering",
            years_experience=2,
        ),
    ]

    mission_data: dict[str, object] = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime.now(),
        "duration_days": 900,
        "crew": crew,
        "budget_millions": 2500.0,
    }

    print("Space Mission Crew Validation")
    print("=========================================")
    valid_mission = SpaceMission.model_validate(mission_data)
    valid_mission.show()

    print("\n=========================================")
    try:
        # This crew has no Commander or Captain.
        SpaceMission.model_validate({**mission_data, "crew": crew[1:]})
    except ValidationError as error:
        print("Expected validation error:")
        for detail in error.errors():
            location = ".".join(str(part) for part in detail["loc"])
            message = detail["msg"].removeprefix("Value error, ")
            print(f"{location + ': ' if location else ''}{message}")


if __name__ == "__main__":
    main()
