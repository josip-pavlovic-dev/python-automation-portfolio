import json
from pathlib import Path
from typing import TypedDict


# Definiši tipove podataka za JSON strukturu
class Settings(TypedDict):
    """Ugnježdeni TypedDict (Nested TypedDict) za podešavanja aplikacije"""
    debug: bool
    timeout: int

class Config(TypedDict):
    """Structura glavnog JSON fajla (config.json)"""
    app_name: str
    version: str
    settings: Settings

def load_config(json_path: Path) -> Config:
    """Učitaj konfiguraciju iz JSON fajla sa tipovima."""
    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)
        # Type checker će osigurati da je data tipa Config
        config: Config = {
            "app_name": data["app_name"],
            "version": data["version"],
            "settings": {
                "debug": data["settings"]["debug"],
                "timeout": data["settings"]["timeout"],
            },
        }
    return config  # Vraća tipiziranu konfiguraciju

def main() -> None:
    json_file = Path(__file__).parent / "type_exercises_data" / "config.json"
    config = load_config(json_file)

    print(f"🔧 Aplikacija: {config['app_name']} v{config['version']}")
    print(f"   Debug: {config['settings']['debug']}")
    print(f"   Timeout: {config['settings']['timeout']}s")

if __name__ == "__main__":
    main()
