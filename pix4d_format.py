import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
args, unknown = parser.parse_known_args()

main_path = f'D:\\PW\\inpho_pix\\pix_proj\\'

for subdir, dirs, files in os.walk(main_path):

    for dir in dirs:
        for subdir_2, dirs_2, files_2 in os.walk(f'{main_path}{dir}'):
            print(f'Current dir is {dir}')
            file_count = 0
            for file_name in files_2:
                file_count += 1
                if file_name.endswith('_calibrated_external_camera_parameters.txt'):
                    file_path = os.path.join(subdir_2,file_name)
                    print(file_path)
                    #with open(file_path, 'r') as f:
                    #    line_lst = list()
                    #    for line in f:
                    #        line_lst.append(line)
#
                    #    for item in line_lst:
                    #        print(item[:-1])
                    df = pd.read_csv(file_path, delimiter=' ')
                    print(df)

