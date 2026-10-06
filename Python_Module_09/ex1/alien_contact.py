from datetime import datetime
from enum import Enum

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    ValidationInfo,
    field_validator,
    model_validator,
)


TELEPATHIC_WITNESS_ERROR = "Telepathic contact requires at least 3 witnesses"


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @field_validator("witness_count")
    @classmethod
    def check_witnesses_telepathic(
        cls, value: int, info: ValidationInfo
    ) -> int:
        # This check can run alongside other field checks.
        if (
            info.data.get("contact_type") == ContactType.TELEPATHIC
            and value < 3
        ):
            raise ValueError(TELEPATHIC_WITNESS_ERROR)
        return value

    @model_validator(mode="after")
    def check_contact_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(TELEPATHIC_WITNESS_ERROR)

        if self.signal_strength > 7.0 and not (
            self.message_received and self.message_received.strip()
        ):
            raise ValueError("Strong signals require a received message")

        return self

    def show(self) -> None:
        print(
            "Alien Contact Log Validation",
            "======================================",
            "Valid contact report:",
            f"ID: {self.contact_id}",
            f"Type: {self.contact_type.value}",
            f"Location: {self.location}",
            f"Signal: {self.signal_strength}/10",
            f"Duration: {self.duration_minutes} minutes",
            f"Witnesses: {self.witness_count}",
            f"Message: {self.message_received!r}",
            f"Verified: {self.is_verified}",
            sep="\n",
        )


def main() -> None:
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        message_received="Greetings from Zeta Reticuli",
        witness_count=5,
    )
    valid_contact.show()

    print("\n======================================")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            contact_type=ContactType.TELEPATHIC,
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            signal_strength=9.0,
            duration_minutes=66,
            message_received="Greetings",
            witness_count=2,
        )
    except ValidationError as error:
        print("Expected validation errors:")
        for detail in error.errors():
            field = ".".join(str(part) for part in detail["loc"]) or "contact"
            reason = detail["msg"].removeprefix("Value error, ")
            print(f"- {field} ({detail['input']!r}): {reason}")


if __name__ == "__main__":
    main()
