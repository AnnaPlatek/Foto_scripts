#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
#from inpho_pix_methods import search_coor_system
#from inpho_pix_methods import search_navigation_params
import pandas as pd

parser = argparse.ArgumentParser()
args, unknown = parser.parse_known_args()

params_pix_path = 'D:\\PW\\inpho_pix\\Malbork_AT\\pix\\Malbork_pix\\1_initial\\params\\'
photos_path = 'D:\\AP\\inpho\\Malbork_AT\\Zdjecia\\'



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



lin_units_obj = 'm'
lin_units_img = 'mm'
ang_units = 'deg'
rpt_log_path = 'C:\\Users\\Student\\new_report.log'
gps_std = ['0.100000', '0.100000', '0.250000']
ins_std = ['0.100000', '0.100000', '0.500000']
photos = 'photos'



#navigation = search_navigation_params(params_pix_path)


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
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_wkt.prj'):
                with open(f'{params_pix_path}{file}', 'r') as coo_sys_f:
                    for line in coo_sys_f:
                        coord_sys = line
    f.write(f'     {coord_sys}\n')

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
    #photo list
    photo_lst = list()
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_calibrated_external_camera_parameters_error.txt'):
                df = pd.read_csv(f'{params_pix_path}{file}', delimiter=', ')

    for index, rows in df.iterrows():
        photo_lst.append(rows.imageName)

    #print(photo_lst)

    #points list
    points_list = list()
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_measured_estimated_gcps_position.txt'):
                df = pd.read_csv(f'{params_pix_path}{file}', delimiter=', ')

    for index, rows in df.iterrows():
        points_list.append(rows['GCP label'])


    #list of measured points on photo
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_tp_orima.txt'):
                points_file = file

    with open(f'{params_pix_path}{points_file}', 'r') as points_f:
        measured_point_lst = list()
        for line in points_f:
            line_item_lst = list()
            split_line = line.split(' ')
            for item in split_line:
                if item not in ['', '\n']:
                    line_item_lst.append(item)
            #print(line_item_lst)
            measured_point_lst.append(line_item_lst)
        #for item in measured_point_lst:
         #   print(item)
        #print(measured_point_lst)

    #photo_constant_params
    #focal lenght
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_calibrated_internal_camera_parameters.cam'):
                with open(f'{params_pix_path}{file}', 'r', encoding='utf-8') as cam_f:
                    for line in cam_f:
                        if line.startswith('FOCAL '):
                            focal_len = line.split(' ')[1]
                            focal_len = focal_len[:-2]

    #write photos params
    for photo in photo_lst:
        #params for individual photo
        #eo
        for subdir, dirs, files in os.walk(params_pix_path):
            for file in files:
                if file.endswith('_calibrated_external_camera_parameters_error.txt'):
                    df = pd.read_csv(f'{params_pix_path}{file}', delimiter=', ')

        for index, rows in df.iterrows():
            if photo == rows.imageName:
                photo_x = rows.X_opt
                photo_y = rows.Y_opt
                photo_z = rows.Z_opt
        #measured control points


        f.write(f'$PHOTO\n')
        f.write(f'  $PHOTO_NUM : {photo[:-4]}\n')
        f.write(f'  $PHOTO_FILE : {photos_path}{photo}\n')
        f.write(f'  $CAMERA_ID : \n')
        f.write(f'  $TERRAIN_HEIGHT : \n')
        f.write(f'  $IO_PARS : \n')
        f.write(f'  $EXT_ORI : \n')
        f.write(f'\t\t{focal_len}\t{photo_x}\t{photo_y}\t{photo_z}\n')

        f.write(f'  $PHOTO_POINTS :\n')
        #for point in points_list:
        #    print(f'point {point}')
        for item in measured_point_lst:
            if photo[:-4] == item[0]:
                for point in points_list:
                    if point == item[1][1:]:
                        f.write(f'    {point}\t{item[3]}\t{item[2]}\t1.00\t2')
                        f.write(' { * }\n')

        f.write(f'  $END_POINTS\n')

        f.write(f'$END\n')
    #nav_gps_lst = list()
    #for index, rows in df.iterrows():
    #    gps_lst = [rows.imageName[:-4], rows.X_gps, rows.Y_gps, rows.Z_gps]
    #    nav_gps_lst.append(gps_lst)


    

    #CAMERA
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_calibrated_internal_camera_parameters.cam'):
                with open(f'{params_pix_path}{file}', 'r', encoding='utf-8') as cam_f:
                    for line in cam_f:
                        if line.startswith('#Image size'):
                            colums_rows_size = line.split(' ')[2]
                            ccd_col = colums_rows_size.split('x')[0]
                            ccd_rows = colums_rows_size.split('x')[1]
                        elif line.startswith('FOCAL '):
                            focal_len = line.split(' ')[1]
                            focal_len = focal_len[:-2]
                        elif '#Principal Point Offset xpoff ypoff in mm (Inpho)' in line:
                            prin_point_PPA_lst = list()
                            prin_point_PPA_lst.append(cam_f.__next__())
                            prin_point_PPA_lst.append(cam_f.__next__())
                            prin_point_PPA_x = prin_point_PPA_lst[0].split(' ')[1]
                            prin_point_PPA_y = prin_point_PPA_lst[1].split(' ')[1]



    #camera_type = 'hasselbladt'
    #camera_date = '14:16:07 25/04/2017'
    #camera_brand = 'Custom'
    #camera_kind = 'CCDFrame'
    #ccd_in_orient = ['-0.0000000000', '-166.6666666667', '4102.1667000000', '-166.6666666667', '-0.0000000000', '3052.7167000000']
    #pxl_ref = 'CenterTopLeft'
    #prin_point_PPA = ['0.000000', '0.000000']
    #gps_antenna_offset = ['0.000000', '0.000000', '0.000000']
    #camera_mount_rotation = '0.000000'

    f.write(f'$CAMERA\n')
    f.write(f'  $TYPE : \n')
    f.write(f'  $DATE : \n')
    f.write(f'  $BRAND : \n')
    f.write(f'  $KIND : \n')
    f.write(f'  $CCD_INTERIOR_ORIENTATION :\n')
    f.write(f'    \n')
    f.write(f'    \n')
    f.write(f'  $CCD_COLUMNS : {ccd_col}\n')
    f.write(f'  $CCD_ROWS : {ccd_rows}\n')
    f.write(f'  $PIXEL_REFERENCE : \n')
    f.write(f'  $FOCAL_LENGTH :    {focal_len}\n')
    f.write(f'  $PRINCIPAL_POINT_PPA :     {prin_point_PPA_x[:-2]} {prin_point_PPA_y[:-2]}\n')
    f.write(f'  $GPS_ANTENNA_OFFSET :     \n')
    f.write(f'  $CAMERA_MOUNT_ROTATION :     \n')
    f.write(f'$END\n')

    #POINTS
    f.write(f'$CONTROL_POINTS\n')
    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_measured_estimated_gcps_position.txt'):
                df = pd.read_csv(f'{params_pix_path}{file}', delimiter=', ')

    points_lst = list()
    for index, rows in df.iterrows():
        f.write(f'  {rows["GCP label"]}\t{rows["GCP measured X"]}\t{rows["GCP measured Y"]}\t{rows["GCP measured Z"]}\t3\t0\t0\t0\n')

    f.write(f'$END_POINTS\n')

    #NAVIGATION
    f.write(f'$NAVIGATION\n')
    #f.write(f'{navigation}\n')

    for subdir, dirs, files in os.walk(params_pix_path):
        for file in files:
            if file.endswith('_calibrated_external_camera_parameters_error.txt'):
                df = pd.read_csv(f'{params_pix_path}{file}', delimiter=', ')

    nav_gps_lst = list()
    for index, rows in df.iterrows():
        gps_lst = [rows.imageName[:-4], rows.X_gps, rows.Y_gps, rows.Z_gps]
        nav_gps_lst.append(gps_lst)
    #print(nav_gps_lst)

    for item in nav_gps_lst:
        f.write(f'  $PHOTO_NUM : {item[0]}\n'
                f'    $GPS :     {item[1]}\t{item[2]}\t{item[3]}\n'
                f'    $INS :     \n')

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








