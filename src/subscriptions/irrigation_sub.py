from gql import gql
import json

# from smart_garden import constants
import sys

sys.path.append("../")
from constants import (
    User_UUID,
    TOKEN,
    HASURA_WSS_ENDPOINT,
    IRRIGATION_TIME_JSON,
    IRRIGATION_TIME_SUBSCRIPTION,
)

from utils import not_connected, get_client


client = get_client(HASURA_WSS_ENDPOINT, TOKEN)

# Provide a GraphQL query
subscription = gql(IRRIGATION_TIME_SUBSCRIPTION)
params = {"u_uuid": User_UUID}

try:
    while not_connected():
        pass
    for result in client.subscribe(subscription, variable_values=params):
        print(json.dumps(result, indent=4, sort_keys=True))
        if result.get("irrigation_timings") is not None:
            with open(IRRIGATION_TIME_JSON, "w") as f:
                json.dump(result, f, indent=4)
except KeyboardInterrupt:
    quit()
except Exception as e:
    print(e)
    quit()
