from numpy import power
from sllurp.reader import R420
from pprint import pprint
import json
import os
import time
import statistics

# import logging

# logging.basicConfig(filename='llrp.log', level=logging.DEBUG)


# in two files named reader.py in the sllurp-measurements folder I have commented out prints for the 
# detectTags function to suppress getting so many lines printed during testing. This is generally a helpful
# print statement though, and should be uncommented for general use. They are found in lines 139 and 273
# of both of these files currently

reader = R420('169.254.1.1')

freqs = reader.freq_table
powers = reader.power_table
mrt_read_duration = 0.5
# num_mrt_readings = int(input('how many sweeps do you want for MRT? '))
num_mrt_readings = 5
# mrt_read_duration = float(input('how fast should we read the mrt? (in seconds): '))
rssi_read_duration = 0.1
num_rssi_readings = 0
# num_rssi_readings = int(input('how many readings do you want for RSSI? '))

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
    },
    'e280689000000001a2f9e49d':
    {
        'tag': 'tag_6',
        'EPC-96': 'e280689000000001a2f9e49d',
        'location': 'bottom_right'
    },
    'e280689000000001a2f9e47f':
    {
        'tag': 'tag_7',
        'EPC-96': 'e280689000000001a2f9e47f',
        'location': 'bottom_left'
    },
    'e280689000000001a2fb6418':
    {
        'tag': 'tag_8',
        'EPC-96': 'e280689000000001a2fb6418',
        'location': 'rim_back'
    }
}

# Note for tag ids, right and left are in the frame of the pot's face
# so if the pot is a person, right is their right arm. left is their left arm


timestr = time.strftime("%Y%m%d-%H%M%S")
print('creating new file structure at data/automated_test/'+timestr)

newpath = './data/automated_test/'+timestr 
if not os.path.exists(newpath):
    os.makedirs(newpath)

locations = ['0deg', '30deg', '60deg', 'front', 'back', 'left', 'right', 'top', 'bottom']
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
    
    print('starting' + str(num_mrt_readings) + 'mrt sweeps for moisture level: '+moisture_level+' and location: '+location)
    for i in range(num_mrt_readings):
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
                    print('\r' + tag['EPC-96'].decode('utf-8') + ' ' + tag_ids[tag['EPC-96'].decode('utf-8')]['location'] + '\t\t\t' + str(powers[j]) + 'dBm')
            if len(tags_found) >= len(tag_ids):
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

    print('\a')
    print('\a')
    print('\a')
    print('\a')
    print('\a')    
    
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
            print('range of mrt readings: ' + str(min(min_Tx_power[tag])) + ' - ' + str(max(min_Tx_power[tag])))
            print('median mrt reading: ' + str(statistics.median(min_Tx_power[tag])))

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    loc_index+=1
    location=locations[loc_index%9]
    print(location)
    moisture_level = input('what is the new moisture level? (done to finish): ')
    # mrt_read_duration = float(input('how fast should we read the mrt? (in seconds): '))
