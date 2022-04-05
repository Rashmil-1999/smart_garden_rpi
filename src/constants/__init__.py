from .auth import TOKEN, HEADERS, User_UUID, HASURA_WSS_ENDPOINT, HASURA_HTTP_ENDPOINT
from .paths import (
    BASE_DIR,
    LOGS,
    CONSTANTS,
    IRRIGATION_TIME_JSON,
    IRRIGATION_CONTROL_JSON,
    IRRIGATION_MODE_JSON,
    PLANT_MAPPING_JSON,
)
from .queries import (
    IRRIGATION_TIME_SUBSCRIPTION,
    MANUAL_CONTROL_SUBSCRIPTION,
    MANUAL_SUBSCRIPTION,
    PLANT_MAPPING_SUBSCRIPTION,
    IRRIGATION_LOG_MUTATION,
    SENSOR_DATA_MUTATION,
)
from .pins import DHT_PIN, STACK, BUZZER_PIN, DS182B0_PIN
