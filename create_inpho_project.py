#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
args, unknown = parser.parse_known_args()

#variables
pix_prj_path = ''
inpho_prj_path = 'D:\\PW\\inpho_pix\\inpho_test\\'
inpho_file_name = 'inpho_test'
user_id = 'student'
starting_date = 'śr. paź 7 12:36:11 2020'
last_change = 'Thu Oct  8 09:59:26 2020'
image_type = 'Aerial'

with open(f'{inpho_prj_path}{inpho_file_name}.prj', 'w+', encoding='utf-8') as f:
    f.write(f'$PROJECT 5.0.0\n')
    f.write(f'  $PROJECT_NAME : {inpho_file_name}\n')
    f.write(f'  $USER_ID : {user_id}\n')
    f.write(f'  $STARTING_DATE : {starting_date}\n')
    f.write(f'  $LAST_CHANGE : {last_change}\n')
    f.write(f'  $IMAGE_TYPE : {image_type}\n')

    f.write(f'  $STD_DEV_OBJECT_POINTS : {}\n')
    f.write(f'  $STD_DEV_OBJECT_Z_POINTS : {}\n')
    f.write(f'  $STD_DEV_IMAGE_POINTS : {}\n')
    f.write(f'  $STD_DEV_IMAGE_GC_POINTS : {}\n')
    f.write(f'  $SDS_OBJ_GROUP_XY :  {}\n')
    f.write(f'  $SDS_OBJ_GROUP_Z :  {}\n')
    f.write(f'  $REFRACT_CORR_DEFAULT : {}\n')
    f.write(f'  $CURV_CORR_DEFAULT : {}\n')
    f.write(f'  $COORDINATE_SYSTEM :\n')

    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')
    f.write(f'{}\n')



