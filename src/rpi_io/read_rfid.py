from typing import List
import telnetlib
import json

from pprint import pprint
import sys

sys.path.append("../")
from constants import RFID_READER, RFID_PORT


reader = telnetlib.Telnet(RFID_READER, RFID_PORT)

data: List[str] = reader.read_until(b" ", timeout=2).decode().split("\r\n")
clean_data: List[dict] = [json.loads(entry) for entry in data if entry != ""]

pprint(clean_data)

pprint([c_d["tid"] for c_d in clean_data])
pprint(len(clean_data))

