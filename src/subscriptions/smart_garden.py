#!/usr/bin/python3
import RPi.GPIO as GPIO
import serial

import time
from typing import List, Dict, Union
import datetime as dt
import logging
import json
import socket
import os
from gql import Client
from pprint import pprint

import constants
import rpi_io

from utils import not_connected
from helper import HasuraClient, sync

# set GPIO Mode to BCM
GPIO.setmode(GPIO.BCM)

# set up logging configuration
logging.basicConfig(
    filename=constants.IRRIGATION_LOG,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# Variable Declarations
# schedule vars
water_schedule: List[str] = []

# flags
manual_mode: bool = constants.manual_mode
manual_control_flag: bool = constants.manual_control_flag
auto_control_flag: bool = constants.auto_control_flag
network_status: bool = constants.network_status

# get last modified time of the files in seconds at the start of the script
manual_file_last_modified: int = constants.manual_file_last_modified
timing_file_last_modified: int = constants.timing_file_last_modified
sensor_mapping_last_modified: int = constants.sensor_mapping_last_modified
manual_control_file_last_modified: int = constants.manual_control_file_last_modified


# try creating remote handler
try:
    remote: Client = HasuraClient(
        url=constants.HASURA_HTTP_ENDPOINT,
        headers=constants.HEADERS,
        U_UUID=constants.User_UUID,
    )
except Exception as e:
    if e.__class__.__name__ == "ConnectionError":
        logging.error("Connection Error, Could not create remote handler.")
    else:
        logging.error(repr(e))
    remote = None


# set the last irrigated value from the file at the start of the script
with open(constants.LAST_IRRIGATED, "r") as f:
    data = f.readline()
last_irrigated = data

# set the last updated sensor values from the file at the start of the script
with open(constants.LAST_SENSOR_DATA_UPDATE, "r") as f:
    data = f.readline()
last_updated_sensor_data = data

##### Data collection #####


def collect_data():
    air_hum, air_temp = rpi_io.read_DHT22()
    amb_light: float = rpi_io.get_light_reading
    lux_light: float = rpi_io.get_lux_reading()
    white_light: float = rpi_io.get_white_light_reading()
    # get soil temperature & moisture
    # compose all the data into proper format and return.


if __name__ == "__main__":
    try:
        # run these commands to enable/start onewire communication
        # os.system("modprobe w1-gpio")
        # os.system("sudo modprobe w1-therm")
        water_schedule, timing_file_last_modified = sync.sync_schedule_settings(
            water_schedule, constants.IRRIGATION_TIME_JSON, timing_file_last_modified
        )
    except KeyboardInterrupt:
        print("Quit")
        # Reset GPIO settings
        GPIO.cleanup()
        quit()
