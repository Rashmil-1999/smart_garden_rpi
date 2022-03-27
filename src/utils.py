from gql import Client
from gql.transport.websockets import WebsocketsTransport
import socket


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

