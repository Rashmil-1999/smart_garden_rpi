""" 
This file is used to detect the amount of light incident on the VEML 7700 Light sensor.

We used the adafruit's VEML 7700 light sensor and use their library to access the sensor
readings.

The sensor directly reads lux values, which is the SI unit of intensity of light.
"""

from typing import Union
import time
import board
import adafruit_veml7700


i2c = board.I2C()  # uses board.SCL and board.SDA

# initialize the light sensor module

try:
    light_sensor = adafruit_veml7700.VEML7700(i2c)
except Exception as e:
    print(
        "Error in initializing the light sensor. Check if it is present on the bus by using\n\nsudo i2cdetect -y 1\n"
    )
    print(e.with_traceback())


def get_light_reading() -> Union[float, None]:
    """get_light_reading returns the ambient light reading from sensor

    Returns
    -------
    Union[float, None]
        Returns the float value of light reading or None
    """
    if light_sensor:
        try:
            light_reading: float = light_sensor.light
        except Exception as e:
            print("Couldn't access light property on light sensor.")
            print(e.with_traceback())
            return None
        return light_reading
    return None


def get_lux_reading() -> Union[float, None]:
    """get_lux_reading returns the intensity of light in SI units

    Returns
    -------
    Union[float, None]
        Returns the float value of light reading or None
    """
    if light_sensor:
        try:
            light_reading: float = light_sensor.lux
        except Exception as e:
            print("Couldn't access lux property on light sensor.")
            print(e.with_traceback())
            return None
        return light_reading
    return None


def get_white_light_reading() -> Union[float, None]:
    """get_white_light_reading returns the white light reading from sensor

    Returns
    -------
    Union[float, None]
        Return the float value of light reading or None
    """
    if light_sensor:
        try:
            light_reading: float = light_sensor.white
        except Exception as e:
            print("Couldn't access white property on light sensor.")
            print(e.with_traceback())
            return None
        return light_reading
    return None


def get_light_sensor_reading(reading: str = "light") -> Union[float, None]:
    """get_light_sensor_reading helper function that reads light sensor reading in specified format

    Parameters
    ----------
    reading : str, optional
        Specifies the type of reading desired by the user, by default "light"

    Returns
    -------
    Union[float, None]
        Return the float value of light reading or None
    """
    if reading == "light":
        return get_light_reading()
    elif reading == "lux":
        return get_lux_reading()
    elif reading == "white":
        return get_white_light_reading()
    else:
        print(
            "Incorrect reading type argument. Permitted values are; \n\t'light', 'lux' and 'white'"
        )


def get_avg_reading(reading: str = "light", t: int = 5) -> Union[float, None]:
    """get_avg_reading gets the average reading of the light intensity in given time t

    Parameters
    ----------
    reading : str, optional
        Specifies the type of reading desired by the user, by default 'light'
    t : int, optional
        Time in seconds for which the average should be taken, by default 5

    Returns
    -------
    Union[float, None]
        Return the float value of light reading or None
    """
    t0 = time.time()
    total_reading = 0
    counter = 0
    while time.time() - t0 < t:
        val = get_light_sensor_reading(reading)
        if val:
            total_reading += val
            counter += 1
        time.sleep(0.1)

    return total_reading / counter
