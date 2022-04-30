from typing import Dict, List, Union

from gql import Client
from gql.transport.websockets import WebsocketsTransport
import socket
import json
import pathlib


def not_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return False
    except OSError:
        pass
    return True


def get_client(
    URI_ENDPOINT: str, token: str, fetch_schema_from_transport: bool = True
) -> Client:
    # Initialize the WebsocketsTransport for subscription to the irrigation_timings table
    transport = WebsocketsTransport(
        url=URI_ENDPOINT, headers={"Authorization": f"Bearer {token}"},
    )

    # Create a GraphQL client using the defined transport
    client = Client(
        transport=transport, fetch_schema_from_transport=fetch_schema_from_transport
    )

    return client


def read_json(filename: Union[pathlib.Path, str]) -> None:
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(filename: Union[pathlib.Path, str], data: dict) -> dict:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
