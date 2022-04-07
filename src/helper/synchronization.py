from typing import List, Tuple
import json
import datetime as dt
import os
from pathlib import Path


def sync_irrigation_timings(IRRIGATION_TIME_JSON: Path) -> List[int]:
    """sync_irrigation_timings reads the irrigation timings updated from 
    the cloud

    Parameters
    ----------
    IRRIGATION_TIME_JSON : Path
        Path to the file where latest data is present

    Returns
    -------
    List[int]
        returns the list of integers denoting irrigation time for each 
        channel in seconds
    """
    with open(IRRIGATION_TIME_JSON) as f:
        data = json.load(f)
    new_timings: List[str] = [
        value
        for key, value in data["irrigation_timings"][0].items()
        if key != "schedule"
    ]
    return new_timings


def sync_schedule_stack(water_schedule: List[str]) -> List[str]:
    """sync_schedule_stack function rotates the scheduling stack to keep the 
    earliest time of watering first

    Parameters
    ----------
    water_schedule : List[str]
        A list of strings which denote the time in 24 Hour format.
        Assumed to be to the perfect hour

    Returns
    -------
    List[str]
        Modified stack is returned if it is not already in the perfect order or
        is left unchanged
    """
    now = int(dt.datetime.now().strftime("%H"))
    water_time_int = [int(time) for time in water_schedule]
    for stack_top in water_time_int:
        if now > stack_top:
            water_schedule.append(water_schedule.pop(0))
        else:
            return water_schedule


def sync_schedule_settings(
    water_schedule: List[str],
    IRRIGATION_TIME_JSON: Path,
    timing_file_last_modified: int,
) -> Tuple[List[str], int]:
    """sync_schedule_settings reads the irrigation timing file to extract schedule 
    for watering

    Parameters
    ----------
    water_schedule : List[str]
        A list of strings which denote the time in 24 Hour format.
        Assumed to be to the perfect hour
    IRRIGATION_TIME_JSON : Path
        Path to the irrigation timing file
    timing_file_last_modified : int
        Value indicating the last modified time of the file

    Returns
    -------
    List[str]
        A list of strings of updated schedule that the system should follow
    """
    modtime = os.stat(IRRIGATION_TIME_JSON)[8]
    if (modtime - timing_file_last_modified) > 0:
        print("Timing file modified, updating schedule...")
        with open(IRRIGATION_TIME_JSON) as f:
            try:
                data = json.load(f)
                water_schedule = data["irrigation_timings"][0]["schedule"].split(":")
                timing_file_last_modified = modtime
                water_schedule = sync_schedule_stack(water_schedule)
            except Exception as e:
                print("Error Syncing timing file.")
                print(e)

    return water_schedule, timing_file_last_modified


# sync sensor status


def sync_manual_settings(
    IRRIGATION_MODE_JSON: Path, manual_mode: bool, manual_file_last_modified: int
) -> Tuple[bool, int]:
    """sync_manual_settings reads the manual mode json file to determine what mode to operate in

    Parameters
    ----------
    IRRIGATION_MODE_JSON : Path
        Path to the manual mode file
    manual_mode : bool
        Flag value to indicate the status of the operational mode
    manual_file_last_modified : int
        Value indicating the last time the file was modified

    Returns
    -------
    Tuple[bool, int]
        Returns the modified values
    """
    modtime = os.stat(IRRIGATION_MODE_JSON)[8]
    if (modtime - manual_file_last_modified) > 0:
        print("\nManual file config modified, updating parameter")
        with open(IRRIGATION_MODE_JSON) as f:
            try:
                data = json.load(f)
                manual_mode = data["irrigation_mode"][0]["manual"]
                manual_file_last_modified = modtime
            except Exception as e:
                print(e)
    return manual_mode, manual_file_last_modified


def sync_manual_control_settings(
    MANUAL_CONTROL_JSON: Path,
    manual_control_data: dict,
    manual_control_file_last_modified: int,
) -> Tuple[dict, int]:
    """sync_manual_control_settings reads the manual control json which
    specifies the time for a channel to stay open when a command is passed

    Parameters
    ----------
    MANUAL_CONTROL_JSON : Path
        Path to the manual mode's control file
    manual_control_data : dict
        Data that is to be modified
    manual_control_file_last_modified : int
        Value indicating the last time the file was modified

    Returns
    -------
    Tuple[dict, int]
        Returns the modified values
    """
    modtime = os.stat(MANUAL_CONTROL_JSON)[8]
    if (modtime - manual_control_file_last_modified) > 0:
        print("Manual Control modified, executing...\n")
        with open(MANUAL_CONTROL_JSON) as f:
            try:
                data = json.load(f)
                manual_control_data = data["irrigation_mode"][0]
                manual_control_file_last_modified = modtime
            except Exception as e:
                print(e)
    return manual_control_data, manual_control_file_last_modified


def reset_manual_control_settings(
    MANUAL_CONTROL_JSON: Path, manual_control_data: dict,
) -> Tuple[dict, int]:
    """reset_manual_control_settings is used to reset all the manual mode irrigation 
    values to 0
    so that they can be ignored

    Parameters
    ----------
    MANUAL_CONTROL_JSON : Path
        Path to the manual mode's control file
    manual_control_data : dict
        Data that is to be reset

    Returns
    -------
    Tuple[dict, int]
        Returns the updated values of control files
    """
    # reset the dictionary of settings to 0 seconds and update the file
    for key, _ in manual_control_data.items():
        manual_control_data[key] = 0
    with open(MANUAL_CONTROL_JSON, "w") as f:
        try:
            f.truncate()
            json.dump({"irrigation_mode": [manual_control_data]}, f)
            manual_control_file_last_modified: int = os.stat(MANUAL_CONTROL_JSON)[8]
            print("Manual Control file reset complete...")
        except Exception as e:
            print("Error in resetting the file")
            print(e)
    return manual_control_data, manual_control_file_last_modified
