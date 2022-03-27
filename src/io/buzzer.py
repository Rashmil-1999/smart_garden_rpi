from typing import List
from gpiozero import Buzzer
from time import sleep
import sys

sys.path.append("../")
from constants import BUZZER_PIN

buzzer = Buzzer(BUZZER_PIN)


def buzz_5() -> None:
    buzzer.on()
    sleep(5)
    buzzer.off()


def buzz_3() -> None:
    buzzer.on()
    sleep(3)
    buzzer.off()


def buzz(t: int) -> None:
    """buzz Turns on the buzzer for given time t

    Parameters
    ----------
    t : int
        Time for the buzzer to stay on in seconds
    """
    if t == 0:
        return
    buzzer.on()
    sleep(t)
    buzzer.off()


def buzz_tune(time_list: List[int], break_list: List[int]) -> None:
    """buzz_tune Turns the buzzer on for given array of times in seconds taking
    b seconds break in between. Length of breaks should be 1 less then length of
    time_list

    Parameters
    ----------
    time_list : List[int]
        Time array for which buzzer should stay on.
    break_list : List[int]
        Time array for which buzzer should stay off.
    """
    if len(time_list) == 0:
        return
    assert len(time_list) == (
        len(break_list) - 1
    ), "The length of break_list should be 1 less then time_list."

    for t in time_list:
        buzz(t)
