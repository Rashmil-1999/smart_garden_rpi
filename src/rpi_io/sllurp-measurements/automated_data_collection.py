from numpy import power
from sllurp.reader import R420
from pprint import pprint
import json
import os
import time

# import logging

# logging.basicConfig(filename='llrp.log', level=logging.DEBUG)


# in two files named reader.py in the sllurp-measurements folder I have commented out prints for the 
# detectTags function to suppress getting so many lines printed during testing. This is generally a helpful
# print statement though, and should be uncommented for general use. They are found in lines 139 and 273
# of both of these files currently

reader = R420('169.254.1.1')

freqs = reader.freq_table
powers = reader.power_table
mrt_read_duration = 0.2
rssi_read_duration = 0.1
num_rssi_readings = 200

#  Do a couple of ten reads to warmup the reader and confirm correct number of tags being read
print('warming up the reader')
for i in range(10):
    reader.detectTags(powerDBm=powers[i*(9)], freqMHz=freqs[0], mode=1002, session=2, population=5, duration=rssi_read_duration, searchmode=2, antennas=(1,))

tag_ids = {
    # 'e280689000000001a2fa42ca':
    # {
    #     'tag': 'tag_1',
    #     'EPC-96': 'e280689000000001a2fa42ca',
    #     'location': 'air'
    # },
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
    },
    'e280689000000001a2f9fb4d':
    {
        'tag': 'tag_5',
        'EPC-96': 'e280689000000001a2f9fb4d',
        'location': 'air'
    }
}

timestr = time.strftime("%Y%m%d-%H%M%S")
print('creating new file structure at data/automated_test/'+timestr)

newpath = './data/automated_test/'+timestr 
if not os.path.exists(newpath):
    os.makedirs(newpath)

locations = ['bottom_boxes', 'mid_boxes', 'top_boxes', 'top_shelf', 'mid_shelf', 'bottom_shelf']
loc_index = 0
location = locations[loc_index]
print(location)
moisture_level = input('what is the moisture level? (done to quit): ')

while(moisture_level != 'done'):

    path = 'data/automated_test/' + timestr + '/' + moisture_level + 'percent' + location + '.json'
    print(path)

    min_Tx_power = {}
    rssi_vals = {}
 
    # loop to sweep the power level up five times and record minimum response threshold transmission power for each 
    
    print('starting mrt sweeps for moisture level: '+moisture_level+' and location: '+location)
    for i in range(5):
        print('sweep number ' + str(i+1))
        tags_found = {}
        for j in range(len(powers)):
            # if j%9 == 0:
                # print('', end='\r')
            print('\r'+str(powers[j]) +' dBm', end=' ')
            tags = reader.detectTags(powerDBm=powers[j], freqMHz=freqs[0], mode=1002, session=2, population=5, duration=mrt_read_duration, searchmode=2, antennas=(1,))
            for tag in tags:
                # pprint(tag)
                if tag['EPC-96'].decode('utf-8') not in tags_found:
                    tags_found[tag['EPC-96'].decode('utf-8')] = 'found'
                    if tag['EPC-96'].decode('utf-8') not in min_Tx_power:
                        min_Tx_power[tag['EPC-96'].decode('utf-8')] = []
                        min_Tx_power[tag['EPC-96'].decode('utf-8')].append(powers[j])
                    else:
                        min_Tx_power[tag['EPC-96'].decode('utf-8')].append(powers[j])
            if len(tags) >= len(tag_ids):
                print('\n')
                break

    # loop to get 1000 readings of rssi fixed at max power level
    print('starting ' + str(num_rssi_readings) + ' readings for rssi')
    for i in range(num_rssi_readings):
        if i%10 == 0:
            # print('', end='\r')
            print('\r' + str(i) + ' / ' +  str(num_rssi_readings), end=' ')
        tags = reader.detectTags(powerDBm=powers[-1], freqMHz=freqs[0], mode=1002, session=2, population=5, duration=rssi_read_duration, searchmode=2, antennas=(1,))
        for tag in tags:
            if tag['EPC-96'].decode('utf-8') not in rssi_vals:
                rssi_vals[tag['EPC-96'].decode('utf-8')] = {
                    'tag_info': tag_ids.get(tag['EPC-96'].decode('utf-8'), None),
                    'peak_rssi': [],
                    'rssi': []
                }
            rssi_vals[tag['EPC-96'].decode('utf-8')]['peak_rssi'].append(tag['PeakRSSI'])
            rssi_vals[tag['EPC-96'].decode('utf-8')]['rssi'].append(tag['RSSI'])


    # pprint(min_Tx_power)
    # pprint(rssi_vals)

    data = {
        'min_Tx_power': min_Tx_power,
        'rssi_vals': rssi_vals
    }

    for i, tag in enumerate(tag_ids):
        print('\n')
        print(tag_ids[tag]['location'])
        if rssi_vals.get(tag, None):
            print('number of rssi readings: ' + str(len(rssi_vals[tag]['peak_rssi'])))
        if min_Tx_power.get(tag, None):
            print('number of mrt readings: ' + str(len(min_Tx_power[tag])))


    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


    loc_index+=1
    location=locations[loc_index%6]
    print(location)
    moisture_level = input('what is the new moisture level? (done to finish): ')