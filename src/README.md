# Smart Garden Project

## Abstract

A regular maintenance schedule and physical access are key requirements for the proper upkeep of house plants. As observed over the past two years, in which the pandemic and other factors have limited our access to places of work and dramatically rearranged our daily routines, our increasingly remote and irregular schedules have interfered with the ability of plant owners to satisfy these requirements. One of the fundamental objectives of this project is to cater to those who desire to have plants in their homes or offices, but because of their busy and irregular schedules don’t indulge in home gardening activities. This project will harnesses the potential of the Hasura GraphQL Engine, Raspberry Pi, various sensors, and a state-of-the-art RFID-based moisture sensing system to build a smart garden.
  
This IoT System will enable the user to remotely access, automatically irrigate, and ensure that house plants are getting an appropriate amount of (artificial) sunlight. Further, this application will provide updates on current system status, notify the user of potential system issues, provide graphical representations of the data collected from various sensors, and allow users to obtain information on the ideal requirements of different plants. This project uses a web-app built in React JS which can be installed on an android phone, granting the users the ability to access the system at their fingertips.

This repository contains the code that resides on Raspberry Pi deployed in the garden.

## Components

| Components                                               | Reason                                                                         |
|----------------------------------------------------------|--------------------------------------------------------------------------------|
| RFID Reader, tags & antenna, Impinj Speedway R420 reader | To read soil moisture using Differential Minimum Response Threshold            |
| DS18B20 Waterproof Temperature sensor                    | To read Soil temperature.                                                      |
| DHT22 Air Temperature and Humidity Sensor                | To read the air humidity and temperature.                                      |
| Raspberry Pi model 3b+                                   | The heart of the garden from where everything is controlled.                   |
| Smart Lights                                             | Off the shelf lights that have the capacity to turn on and off based on timer. |
| 12V DC Relay Hat                                         | This controls the solenoid valves.                                             |
| Water tanks                                              | This tank is used to hold water for irrigation.                                |
| Adafruit VEML7700 Lux Sensor                             | To measure the intensity of the light on the plants.                           |
| 12" eTape, Liquid level sensor                           | To keep track of the water left in the tanks.                                  |
| Passive Buzzer                                           | To give auditory feedback when a certain operation is carried out.             |
| Water Pump                                               | To transfer the water from the lower tank to the upper tank.                   |
| 12V Solenoid Valves                                      | To control the flow of water into the plants.                                  |

## Setup

To install the packages run `pip install -r requirements.txt`

## Files

- `constants` folder contains all the variable declarations that are used across the entire project.

- `helper` folder contains all the utility based functions that help achieve various repetitive tasks.

- `logs` folder is used to keep track of all the error/debug messages along with keeping track of various system states and variables on a persistant storage.

- `rpi_io` folder contains all the sensor functions that can be used to extract data from the sensor, process it and return the values to the caller.

- `rpi_io/sllurp-measurements` folder contains all the files that help in reading moisture from the soil using RFID Reader.

- `services` folder contains all the `.service` files that are `systemctl processes` that manage various python scripts.

- `Soil_mois` folder contains the arduino file that reads the Capacitive Soil Moisture sensor, Water tank Level Sensors.

- `subscriptions` folder contains python script that maintains key functionalities such as:
  - Manual Irrigation Control
  - Manual Mode Control
  - Plant Tracking
  - Irrigation Control

## Execution

The values in `constants` folder needs to be changed for auth, and paths to reflect the user's system.

- The User token in `auth.py`
- `BASE_DIR` in `paths.py`
- `RFID_READER` and `RFID_PORT` variables need to be configured to reflect your reader's settings.
- Once the remote hasura instance has been set up, change the uri pointing to your new endpoint in the variable `HASURA_WSS_ENDPOINT` and `HASURA_HTTP_ENDPOINT`.
- Move all the service files to the folder `/usr/lib/systemd/`
- Then, enable all these services by running `enable.sh`
- Finally, you can now simply run all the services `start.sh`
- To check the status of all the services run `status.sh`

## Setup images

![The setup includes a shelf, pots and the 2 water tanks used to water the plants](./assets/complete_setup.jpg "Complete setup")

![The Pi setup ](./assets/pi_setup.jpg "Pi setup")

![The tanks setup ](./assets/tank.jpg "Tanks setup")

## System Overview

![The System Overview.](./assets/overview.png)

## Modules in the Smart Garden

![The Improved modules in the system are as follows.](./assets/improved_modules.png)

## User Web Communication

![The User web communications.](./assets/user_web_comm.png)

## Circuit diagrams

![Soil Temperature sensor connection.](./assets/soil_temperature_sensor_circuit_diagram.png)
![Solenoid Valve connection diagram.](./assets/solenoid_valve_circuit_diagram.png)

## Main script flow

![Flow chart of the main irrigation script.](./assets/main_script_flow.png)
