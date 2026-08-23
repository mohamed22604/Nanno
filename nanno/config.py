import os
from pathlib import Path
from getpass import getpass
from dotenv import load_dotenv


CONFIG_DIR = Path.home() / ".config" / "nanno"
ENV_FILE = CONFIG_DIR / ".env"


def get_api_key():
    if ENV_FILE.exists():
        load_dotenv(ENV_FILE)

    api_key = os.getenv("NANNO_API_KEY")

    if api_key:
        return api_key

    api_key = getpass("Enter your API key: ")

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    ENV_FILE.write_text(
        f"NANNO_API_KEY={api_key}\n"
    )

    return api_key