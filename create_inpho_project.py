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
std_dev_obj_points = '0.000000'
std_dev_obj_z_points = '0.000000'
std_dev_img_points = '0.000000'
std_dev_img_gc_points = '0.000000'
sds_obj_gr_xy = ['-1.000000', '-1.000000', '-1.000000', '-1.000000']
sds_obj_gr_z = ['-1.000000', '-1.000000', '-1.000000', '-1.000000']
refract_cord_default = 'on'
curv_cord_default = 'on'
coord_sys = ''
lin_units_obj = 'm'
lin_units_img = 'mm'
ang_units = 'deg'
rpt_log_path = 'C:\\Users\\Student\\new_report.log'
gps_std = ['0.100000', '0.100000', '0.250000']
ins_std = ['0.100000', '0.100000', '0.500000']
photos = 'photos'

camera_type = 'hasselbladt'
camera_date = '14:16:07 25/04/2017'
camera_brand = 'Custom'
camera_kind = 'CCDFrame'
ccd_in_orient = ['-0.0000000000', '-166.6666666667', '4102.1667000000', '-166.6666666667', '-0.0000000000', '3052.7167000000']
ccd_col = '8176'
ccd_rows = '6132'
pxl_ref = 'CenterTopLeft'
focal_len = '50.175400'
prin_point_PPA = ['0.000000', '0.000000']
gps_antenna_offset = ['0.000000', '0.000000', '0.000000']
camera_mount_rotation = '0.000000'

navigation = ''


with open(f'{inpho_prj_path}{inpho_file_name}.prj', 'w+', encoding='utf-8') as f:

    #PROJECT SETTINGS
    f.write(f'$PROJECT 5.0.0\n')
    f.write(f'  $PROJECT_NAME : {inpho_file_name}\n')
    f.write(f'  $USER_ID : {user_id}\n')
    f.write(f'  $STARTING_DATE : {starting_date}\n')
    f.write(f'  $LAST_CHANGE : {last_change}\n')
    f.write(f'  $IMAGE_TYPE : {image_type}\n')
    f.write(f'  $STD_DEV_OBJECT_POINTS : {std_dev_obj_points}\n')
    f.write(f'  $STD_DEV_OBJECT_Z_POINTS : {std_dev_obj_z_points}\n')
    f.write(f'  $STD_DEV_IMAGE_POINTS : {std_dev_img_points}\n')
    f.write(f'  $STD_DEV_IMAGE_GC_POINTS : {std_dev_img_gc_points}\n')
    f.write(f'  $SDS_OBJ_GROUP_XY :  {sds_obj_gr_xy[0]} {sds_obj_gr_xy[1]} {sds_obj_gr_xy[2]} {sds_obj_gr_xy[3]}\n')
    f.write(f'  $SDS_OBJ_GROUP_Z :  {sds_obj_gr_z[0]} {sds_obj_gr_z[1]} {sds_obj_gr_z[2]} {sds_obj_gr_z[3]}\n')
    f.write(f'  $REFRACT_CORR_DEFAULT : {refract_cord_default}\n')
    f.write(f'  $CURV_CORR_DEFAULT : {curv_cord_default}\n')
    f.write(f'  $COORDINATE_SYSTEM :\n')
    f.write(f'{coord_sys}\n')
    f.write(f'  $LINEAR_UNITS_OF_OBJECT : {lin_units_obj}\n')
    f.write(f'  $LINEAR_UNITS_OF_IMAGE : {lin_units_img}\n')
    f.write(f'  $ANGULAR_UNITS : {ang_units}\n')
    f.write(f'  $REPORT_LOGFILE : {rpt_log_path}\n')
    f.write(f'$END\n')

    #AAT
    f.write(f'$AAT\n')
    f.write(f'  $GPS_STD : {gps_std[0]} {gps_std[1]} {gps_std[2]}\n')
    f.write(f'  $INS_STD : {ins_std[0]} {ins_std[1]} {ins_std[2]}\n')
    f.write(f'$END\n')

    #PHOTO
    f.write(f'{photos}\n')

    #CAMERA
    f.write(f'$CAMERA\n')
    f.write(f'  $TYPE : {camera_type}\n')
    f.write(f'  $DATE : {camera_date}\n')
    f.write(f'  $BRAND : {camera_brand}\n')
    f.write(f'  $KIND : {camera_kind}\n')
    f.write(f'  $CCD_INTERIOR_ORIENTATION :\n')
    f.write(f'    {ccd_in_orient[0]} {ccd_in_orient[1]} {ccd_in_orient[2]}\n')
    f.write(f'    {ccd_in_orient[3]} {ccd_in_orient[4]} {ccd_in_orient[5]}\n')
    f.write(f'  $CCD_COLUMNS : {ccd_col}\n')
    f.write(f'  $CCD_ROWS : {ccd_rows}\n')
    f.write(f'  $PIXEL_REFERENCE : {pxl_ref}\n')
    f.write(f'  $FOCAL_LENGTH :    {focal_len}\n')
    f.write(f'  $PRINCIPAL_POINT_PPA :     {prin_point_PPA[0]} {prin_point_PPA[0]}\n')
    f.write(f'  $GPS_ANTENNA_OFFSET :     {gps_antenna_offset[0]} {gps_antenna_offset[1]} {gps_antenna_offset[2]}\n')
    f.write(f'  $CAMERA_MOUNT_ROTATION :     {camera_mount_rotation}\n')
    f.write(f'$END\n')

    #POINTS
    f.write(f'$ADJUSTED_POINTS\n')
    f.write(f'$END_POINTS\n')

    #NAVIGATION
    f.write(f'$NAVIGATION\n')
    f.write(f'{navigation}\n')
    f.write(f'$ENDNAV\n')
    f.write(f"""$DESCRIPTIONS
      0 Undefined
      1 Signalized\ Point
      2 Road\ Intersection
      3 Traffic-line\ Marking
      4 Parking\ Lot\ Marking
      5 Corner\ Of\ Pattern
      6 Ground\ Corner
      7 Cottage
      8 Bridge
      9 Pit
     10 Wall\ Corner
     11 House\ Corner
     12 Roof\ Corner
     13 Fence\ Corner
     14 Stone
     15 Thicket
     16 White\ Spot
     17 Dark\ Spot
     18 Sharp\ Bend
$END\n""")








