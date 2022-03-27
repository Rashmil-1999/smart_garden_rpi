""" 
This version of Smart garden assumes we are only dealing with stack 0 of the relay Hat
hence only 8 channels. Therefore, we default the value of STACK to 0. In future, you might
want to add looping of selection logic too. refer to lib8relind and libioplus docs on github
lib8relind: https://github.com/SequentMicrosystems/8relind-rpi/tree/main/python
libioplus: https://github.com/SequentMicrosystems/ioplus-rpi/tree/master/python
"""

import lib8relind as rel

import sys

sys.path.append("../")
from constants import STACK


def on(relay_channel: int) -> None:
    try:
        rel.set(STACK, relay_channel, 1)
    except Exception as e:
        print(e)


def off(relay_channel: int) -> None:
    try:
        rel.set(STACK, relay_channel, 0)
    except Exception as e:
        print(e)


def status(relay_channel: int) -> int:
    """status gets the status of the relay switches

    Parameters
    ----------
    relay_channel : int
        The channel Number of the Relay whose status 
        is to be checked

    Returns
    -------
    int
        1 if that channel is on otherwise 0 if off
    """
    try:
        status = rel.get(STACK, relay_channel)
    except Exception as e:
        print(e)

    return status


def board_status() -> int:
    """board_status returns 1 if any relay switch is on otherwise 0

    Returns
    -------
    int
        1 if any switch is on otherwise 0
    """
    try:
        status = rel.get_all(STACK)
    except Exception as e:
        print(e)

    return status
