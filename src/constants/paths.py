import pathlib

# BASE_DIR: pathlib.Path = pathlib.Path("/home/pi/Desktop/smart_garden")
BASE_DIR: pathlib.Path = pathlib.Path("/Users/rashmilpanchani/Documents/Projects/smart_garden/src")
LOGS: pathlib.Path = BASE_DIR / "logs"
CONSTANTS: pathlib.Path = BASE_DIR / "constants"

IRRIGATION_TIME_JSON: pathlib.Path = LOGS / "irrigation_time.json"
