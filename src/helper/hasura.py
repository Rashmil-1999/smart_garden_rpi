from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
# import datetime as dt

from constants import (
    User_UUID,
    HEADERS,
    IRRIGATION_LOG_MUTATION,
    SENSOR_DATA_MUTATION,
    HASURA_HTTP_ENDPOINT,
)


class HasuraClient:
    def __init__(self, fetch_schema_from_transport=True):
        self.transport = RequestsHTTPTransport(
            url=HASURA_HTTP_ENDPOINT, retries=3, headers=HEADERS
        )
        self.client = Client(
            transport=self.transport,
            fetch_schema_from_transport=fetch_schema_from_transport,
        )
        self.U_UUID = User_UUID
        self.SENSOR_DATA_MUTATION = SENSOR_DATA_MUTATION
        self.IRRIGATION_LOG_MUTATION = IRRIGATION_LOG_MUTATION

    def execute_normal_query(self, query, params):
        return self.client.execute(query, variable_values=params)

    def update_irrigation_log(self, time, mode):
        params = {"u_uuid": self.U_UUID, "time": time, "mode": mode}
        return self.client.execute(self.IRRIGATION_LOG_MUTATION, variable_values=params)

    def insert_sensor_data(self, data):
        return self.client.execute(
            self.SENSOR_DATA_MUTATION, variable_values={"objects": data}
        )


if __name__ == "__main__":
    import datetime as dt

    # params = {
    #     "u_uuid": User_UUID,
    #     "time": str(dt.datetime.now()),
    # }
    try:
        remote = HasuraClient()
    except Exception as e:
        print(e.__class__.__name__ == "ConnectionError")

    try:
        remote.update_irrigation_log(time=str(dt.datetime.now()))
    except Exception as e:
        print("Connection Error")
