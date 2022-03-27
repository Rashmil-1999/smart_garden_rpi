from typing import Tuple
import Adafruit_DHT22
import time
import sys

sys.path.append("../")
from constants import DHT_PIN

DHT_sensor = Adafruit_DHT.DHT22

# function to read temp and humidity in air
def read_DHT22() -> Tuple[float, float]:
    """read_DHT22 reads the Air Temperature and Humidity Readings

    Returns
    -------
    Tuple[float, float]
        Returns a tuple of floats indicating (humidity, temperature)
    """

    hum, temp = Adafruit_DHT.read(DHT_sensor, DHT_PIN)
    if hum is None and temp is None:
        while hum is None and temp is None:
            hum, temp = Adafruit_DHT.read(DHT_sensor, DHT_PIN)
            time.sleep(1)
    return hum, temp
