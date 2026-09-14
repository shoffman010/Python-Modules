import os
import site
import sys


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print(
            "MATRIX STATUS: You're still plugged in",
            "",
            f"Current Python: {sys.executable}",
            "Virtual Environment: None detected",
            "",
            "WARNING: You're in the global environment!",
            "The machines can see everything you install.",
            "",
            "To enter the construct, run:",
            "python -m venv matrix_env",
            "source matrix_env/bin/activate # On Unix",
            r"matrix_env\Scripts\activate # On Windows",
            "",
            "Then run this program again.",
            sep="\n"
        )

    else:
        venv_name = os.path.basename(os.path.normpath(sys.prefix))
        package_path = site.getsitepackages()[0]
        print(
            "MATRIX STATUS: Welcome to the construct",
            "",
            f"Current Python: {sys.executable}",
            f"Virtual Environment: {venv_name}",
            f"Environment Path: {sys.prefix}",
            "",
            "SUCCESS: You're in an isolated environment!",
            "Safe to install packages without affecting",
            "the global system.",
            "",
            "Package installation path:",
            package_path,
            sep="\n"
        )


if __name__ == "__main__":
    main()
