from sllurp.reader import R420
from pprint import pprint
import json
# import logging

# logging.basicConfig(filename='llrp.log', level=logging.DEBUG)

reader = R420('169.254.1.1')

freqs = reader.freq_table
powers = reader.power_table

tag_ids = {
    'e280689000000001a2fa42ca':
    {
        'tag': 'tag_1',
        'EPC-96': 'e280689000000001a2fa42ca',
        'location': 'air'
    },
    'e280689000000001a2f9e48e':
    {
        'tag': 'tag_2',
        'EPC-96': 'e280689000000001a2f9e48e',
        'location': 'rim'
    },
    'e280689000000001a33707c4':
    {
        'tag': 'tag_3',
        'EPC-96': 'e280689000000001a33707c4',
        'location': 'bottom_front'
    },
    'e280689000000001a2fa42ac':
    {
        'tag': 'tag_4',
        'EPC-96': 'e280689000000001a2fa42ac',
        'location': 'bottom_back'
    }
}

path = 'data/90percent/bottom_boxes.json'
print(path)

min_Tx_power = {}
rssi_vals = {}
for i in range(len(powers)):
    print('progress ', i)
    tags = reader.detectTags(powerDBm=powers[i], freqMHz=freqs[0], mode=1002, session=2, population=5, duration=0.5, searchmode=2, antennas=(1,))
    for tag in tags:
        if tag['EPC-96'].decode('utf-8') not in min_Tx_power:
            min_Tx_power[tag['EPC-96'].decode('utf-8')] = powers[i]
        if tag['EPC-96'].decode('utf-8') not in rssi_vals:
            rssi_vals[tag['EPC-96'].decode('utf-8')] = {
                'tag_info': tag_ids.get(tag['EPC-96'].decode('utf-8'), None),
                'peak_rssi': {},
                'rssi': {}
            }
        rssi_vals[tag['EPC-96'].decode('utf-8')]['peak_rssi'][powers[i]] = tag['PeakRSSI']
        rssi_vals[tag['EPC-96'].decode('utf-8')]['rssi'][powers[i]] = tag['RSSI']
        

pprint(min_Tx_power)
# pprint(rssi_vals)

data = {
    'min_Tx_power': min_Tx_power,
    'rssi_vals': rssi_vals
}

with open(path, 'w') as f:
    json.dump(data, f, indent=4)
