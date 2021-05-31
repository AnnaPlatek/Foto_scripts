import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
args, unknown = parser.parse_known_args()

main_path = f'D:\\PW\\inpho_pix\\INPHO-WGPN\\'
with open(f'{main_path}190390_WgPN_RGBI_2020.prj', 'r') as f:
    foto_list = list()
    line_lst = list()
    print_line = False
    for line in f:
        print(f"###{line}### --- ###$PHOTO\n###")
        #print(print_line)
        if line == f'$PHOTO\n':
            print_line = True
        if print_line == True:
            line_lst.append(line)
        if line == '$END\n':
            print_line = False
            foto_list.append(line_lst)
            line_lst = list()

    for item in foto_list:
        if len(item) > 0:
            print(f'{item[2]}\t{item[10]}')
    #print(line_lst)