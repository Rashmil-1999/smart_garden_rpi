import serial
import time
from datetime import datetime


try:
    # set up serial communication on port ACM0 at 9600 baud rate
    ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
    ser.flush()
except Exception as e:
    print("Arduino not present at /dev/ttyUSB0")


# function to read soil_moisture
def read_soil_moisture():
    ser.write(b"moisture\n")
    time.sleep(1)
    read_serial = ser.readlines()[-1].decode("UTF-8")[:-2]
    read_serial = read_serial.split(":")
    soil_moisture = {}
    for i in range(0, len(read_serial), 2):
        soil_moisture[read_serial[i]] = int(int(read_serial[i + 1]) % 100)
    return soil_moisture


if __name__ == "__main__":
    while True:
        data = read_soil_moisture()
        with open("moisture_over_time.txt", "a") as f:
            f.write(str(datetime.now()))
            f.write("\t")
            f.write(str(data))
            f.write("\n")
        time.sleep(1800)
