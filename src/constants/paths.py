import pathlib

# Base Paths
BASE_DIR: pathlib.Path = pathlib.Path("/home/pi/Desktop/smart_garden_rpi/src")
# BASE_DIR: pathlib.Path = pathlib.Path(
#     "/Users/rashmilpanchani/Documents/Projects/smart_garden/src"
# )
LOGS: pathlib.Path = BASE_DIR / "logs"
CONSTANTS: pathlib.Path = BASE_DIR / "constants"
DATA: pathlib.Path = BASE_DIR / "data"

# JSON paths
IRRIGATION_TIME_JSON: pathlib.Path = LOGS / "irrigation_time.json"
IRRIGATION_CONTROL_JSON: pathlib.Path = LOGS / "manual_control.json"
IRRIGATION_MODE_JSON: pathlib.Path = LOGS / "manual_mode.json"
PLANT_MAPPING_JSON: pathlib.Path = LOGS / "plant_mapping.json"

# Log paths
IRRIGATION_LOG: pathlib.Path = LOGS / "irrigation.log"

# Text file paths
LAST_SENSOR_DATA_UPDATE: pathlib.Path = LOGS / "last_sensor_data_updated.txt"
LAST_IRRIGATED: pathlib.Path = LOGS / "last_irrigated.txt"
PENDING_UPDATES: pathlib.Path = LOGS / "pending_update.txt"

# RFID Data

RFID_DATA_FOLDER: pathlib.Path = BASE_DIR / "rpi_io" / "sllurp-measurements" / "data"
