from typing import List

import json
import pathlib
import telnetlib

from pprint import pprint
import sys

sys.path.append("../")
from constants import RFID_READER, RFID_PORT, DATA


reader = telnetlib.Telnet(RFID_READER, RFID_PORT)

data: List[str] = reader.read_until(b" ", timeout=2).decode().split("\r\n")
clean_data: List[dict] = [json.loads(entry) for entry in data if entry != ""]

pprint([c_d["tid"] for c_d in clean_data])
pprint(len(clean_data))

output_file_path: pathlib.Path = DATA / "test.json" 

with open(output_file_path, "w") as f:
    json.dump(clean_data, f, indent=4)
