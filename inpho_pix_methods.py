#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
import pandas as pd

params_pix_path = 'D:\\PW\\inpho_pix\\Malbork_AT\\pix\\Malbork_pix\\1_initial\\params\\'


#navigation
#def search_navigation_params(params_pix_path):
#    for subdir, dirs, files in os.walk(params_pix_path):
#        for file in files:
#            if file.endswith('_calibrated_external_camera_parameters_error.txt'):
#                df = pd.read_csv(f'{params_pix_path}{file}', delimiter=', ')
#
#    nav_gps_lst = list()
#    for index, rows in df.iterrows():
#        gps_lst = [rows.imageName[:-4], rows.X_gps, rows.Y_gps, rows.Z_gps]
#        nav_gps_lst.append(gps_lst)
#    print(nav_gps_lst)
#
#    nav_text = str()
#
#    for item in nav_gps_lst:
#        return (f'  $PHOTO_NUM : {item[0]}\n'
#              f'    $GPS :     {item[1]}\t{item[2]}\t{item[3]}')

#photo

#import coord system
def search_coor_system(params_pix_path):
    for subdir, dirs, files in os.walk(params_pix_path):
       for file in files:
           if file.endswith('_wkt.prj'):
               with open(f'{params_pix_path}{file}', 'r') as f:
                   for line in f:
                       return line
