"""Read Matrix configuration without exposing credentials in program output."""

import os
import sys


CONFIG_KEYS: tuple[str, ...] = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)
LOG_LEVELS: tuple[str, ...] = (
    "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
)
EXAMPLE_VALUES: dict[str, str] = {
    "DATABASE_URL": "replace-with-your-database-url",
    "API_KEY": "replace-with-your-api-key",
    "ZION_ENDPOINT": "replace-with-your-zion-endpoint",
}


def value_source(name: str, process_keys: set[str]) -> str:
    """Describe where a setting came from without showing its value."""
    if not os.getenv(name):
        return "default"
    if name in process_keys:
        return "process environment"
    if name in os.environ:
        return ".env file"
    return "default"


def main() -> int:
    """Load, display, and validate the configuration."""
    print("ORACLE STATUS: Reading the Matrix...\n")

    try:
        from dotenv import load_dotenv
    except ImportError:
        print("python-dotenv is required to read .env files.")
        print("Install it with: python -m pip install python-dotenv")
        return 1

    process_keys: set[str] = set(os.environ).intersection(CONFIG_KEYS)
    env_path: str = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.isfile(env_path):
        try:
            loaded: bool = load_dotenv(dotenv_path=env_path, override=False)
        except (OSError, UnicodeError) as error:
            print(f"Could not read .env file: {error}")
            return 1
        if loaded:
            print("Local .env file: loaded")
        else:
            print("Local .env file: present, but no settings loaded")
    else:
        print("Local .env file: absent")
        print("For development, copy .env.example to .env.")

    mode: str = os.getenv("MATRIX_MODE") or "development"
    if mode not in ("development", "production"):
        print("Invalid MATRIX_MODE: use development or production.")
        return 1

    log_level: str = os.getenv("LOG_LEVEL") or (
        "DEBUG" if mode == "development" else "INFO"
    )
    if log_level not in LOG_LEVELS:
        print("Invalid LOG_LEVEL.")
        print("Use DEBUG, INFO, WARNING, ERROR, or CRITICAL.")
        return 1
    config: dict[str, str] = {
        "DATABASE_URL": os.getenv("DATABASE_URL") or "",
        "API_KEY": os.getenv("API_KEY") or "",
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT") or "",
    }

    print("\nConfiguration loaded:")
    print(f"Mode: {mode} ({value_source('MATRIX_MODE', process_keys)})")
    log_source: str = value_source("LOG_LEVEL", process_keys)
    print(f"Log level: {log_level} ({log_source})")
    for name, label in (
        ("DATABASE_URL", "Database URL"),
        ("API_KEY", "API key"),
        ("ZION_ENDPOINT", "Zion endpoint"),
    ):
        if not config[name]:
            status: str = "missing"
        elif config[name] == EXAMPLE_VALUES[name]:
            status = "example placeholder"
        else:
            status = "configured (value hidden)"
        source: str = (
            value_source(name, process_keys) if config[name] else "unset"
        )
        print(f"{label}: {status} ({source})")

    if mode == "development":
        print("Profile: development")
        print("Policy: demonstration API key permitted.")
    else:
        print("Profile: production")
        print("Policy: demonstration API key rejected.")

    missing: list[str] = [name for name, value in config.items() if not value]
    if missing:
        print("\nMissing required configuration: " + ", ".join(missing))
        return 1

    placeholders: list[str] = [
        name for name, value in config.items()
        if value == EXAMPLE_VALUES[name]
    ]
    if placeholders:
        print("\nReplace example placeholders: " + ", ".join(placeholders))
        return 1

    example_key: bool = config["API_KEY"] == "development-example-key"
    if mode == "production" and example_key:
        print("\nThe example API key is not valid for production.")
        return 1

    if example_key:
        print("\nThe example API key is for local demonstrations only.")

    print("\nThe Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
