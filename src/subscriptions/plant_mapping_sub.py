from gql import gql
import json

# from smart_garden import constants
import sys

sys.path.append("../")
from constants import (
    User_UUID,
    TOKEN,
    HASURA_WSS_ENDPOINT,
    PLANT_MAPPING_JSON,
    PLANT_MAPPING_SUBSCRIPTION,
)

from utils import not_connected, get_client


client = get_client(HASURA_WSS_ENDPOINT, TOKEN)

# Provide a GraphQL query
subscription = gql(PLANT_MAPPING_SUBSCRIPTION)
params = {"u_uuid": User_UUID}

try:
    while not_connected():
        pass
    for result in client.subscribe(subscription, variable_values=params):
        print(json.dumps(result, indent=4, sort_keys=True))
        if result.get("plant_sensor_mapping") is not None:
            with open(PLANT_MAPPING_JSON, "w") as f:
                json.dump(result, f, indent=4)
except KeyboardInterrupt:
    quit()
except Exception as e:
    print(e)
    quit()
