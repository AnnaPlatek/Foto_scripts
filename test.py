#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path as path
import pandas as pd

main_path = "D:\\PW\\SkySNAP\\export_ref_markers\\"

file_lst = list()
for subdir, dirs, files in os.walk(main_path):
    for file in files:
        if file.endswith('.xml'):
            file_lst.append(file)
print(file_lst)

#for file in file_lst:
photo_dict = dict()
point_dict = dict()
measured_point_lst = list()

file='markers_A1_h2.xml'

with open(f'{main_path}{file}', 'r') as f:
    for line in f:
        if line.startswith('        <camera id="'):
            camera_id_record = line.split(' ')[-4]
            camera_id = camera_id_record.split('"')[1]
            camera_label_record = line.split(' ')[-1]
            camera_label = camera_label_record.split('"')[1]
            #temp_list = [camera_id, camera_label]
            #photo_temp_lst.append(temp_list)
            photo_dict[camera_id] = camera_label
        elif line.startswith('      <marker id="'):
            point_id_record = line.split(' ')[-2]
            point_id = point_id_record.split('"')[1]
            point_label_record = line.split(' ')[-1]
            point_label = point_label_record.split('"')[1]
            #temp_list = [point_id, point_label]
            #point_temp_lst.append(temp_list)
            point_dict[point_id] = point_label
        elif line.startswith('          <marker marker_id=') and not line.endswith('/>\n'):
            point_id = line.split('=')[1].replace('"','').replace('>','').replace('/', '').rstrip()
            for inside_line in f:
                if inside_line.startswith('            <location '):
                    temp_lst = list()
                    camera_id = inside_line.split(' ')[-4].replace('camera_id=', '').replace('"', '')
                    x = inside_line.split(' ')[-2].replace('x=', '').replace('"', '')
                    y = inside_line.split(' ')[-1].replace('y=', '').replace('"', '').replace('/>', '').rstrip()
                    #print(camera_id, point_id, x, y)
                    temp_lst = [f'{photo_dict[camera_id]}.JPG', f'{point_dict[point_id]}', x, y]
                    measured_point_lst.append(temp_lst)
                elif inside_line.endswith('/>\n'):
                    break
                elif inside_line.startswith('          </marker>'):
                    break

    if path.exists(f'{main_path}{file[:-4]}.txt') == False:
        with open(f'{main_path}{file[:-4]}.txt', 'x') as f_txt:
            for item in measured_point_lst:
                f_txt.write(f'{item[0]},{item[1]},{item[2]},{item[3]}\n')
    elif path.exists(f'{main_path}{file[:-4]}.txt') == True:
        with open(f'{main_path}{file[:-4]}.txt', 'w') as f_txt:
            for item in measured_point_lst:
                f_txt.write(f'{item[0]},{item[1]},{item[2]},{item[3]}\n')
print(photo_dict)
print(point_dict)
print(measured_point_lst)



