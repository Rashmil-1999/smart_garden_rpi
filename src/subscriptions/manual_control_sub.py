from gql import gql
import json

# from smart_garden import constants
import sys

sys.path.append("../")
from constants import (
    User_UUID,
    TOKEN,
    HASURA_WSS_ENDPOINT,
    IRRIGATION_CONTROL_JSON,
    MANUAL_CONTROL_SUBSCRIPTION,
)
from utils import not_connected, get_client

client = get_client(HASURA_WSS_ENDPOINT, TOKEN)

subscription = gql(MANUAL_CONTROL_SUBSCRIPTION)
params = {"u_uuid": User_UUID}

try:
    while not_connected():
        pass
    for result in client.subscribe(subscription, variable_values=params):
        print(json.dumps(result, indent=4, sort_keys=True))
        if result.get("irrigation_mode") is not None:
            with open(IRRIGATION_CONTROL_JSON, "w") as f:
                json.dump(result, f, indent=4)
except KeyboardInterrupt:
    quit()
except Exception as e:
    print(e)
    quit()

