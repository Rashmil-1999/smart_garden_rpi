from typing import List
import telnetlib
import json

from pprint import pprint

from constants import RFID_READER, RFID_PORT


reader = telnetlib.Telnet(RFID_READER, RFID_PORT)

data: List[str] = reader.read_until(b" ", timeout=2).decode().split("\r\n")
clean_data: List[dict] = [json.loads(entry) for entry in data if entry != ""]

pprint(clean_data)

