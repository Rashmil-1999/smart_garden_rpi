from typing import List
import telnetlib
import json
from statistics import mean

from pprint import pprint
import sys

sys.path.append("../")
from constants import RFID_READER, RFID_PORT


reader = telnetlib.Telnet(RFID_READER, RFID_PORT)

data: List[str] = reader.read_until(b" ", timeout=2).decode().split("\r\n")
clean_data: List[dict] = [json.loads(entry) for entry in data if entry != ""]


tag_set = set([c_d["tid"] for c_d in clean_data])
tag_stats = {}

print('tags:')
pprint(set([c_d["tid"] for c_d in clean_data]))
print('number of readings:')
pprint(len(clean_data))

for tag in tag_set:
    tag_rssi_vals = []
    for c_d in clean_data:
        if c_d['tid'] == tag:
            tag_rssi_vals.append(c_d['peakRssi'])
    tag_stats[tag] = [mean(tag_rssi_vals), min(tag_rssi_vals), max(tag_rssi_vals)]

print('tag, [mean, min, max]')
pprint(tag_stats)

