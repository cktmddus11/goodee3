'''
Created on 2020. 1. 22.

@author: GDJ_19
pandas 모듈을 이용하여 csv 파일을 읽고 쓰기
supplier_data.csv 다운받기
'''

import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out2.csv"

data_frame = pd.read_csv(input_file)
data_frame_in_set = \
data_frame.loc[data_frame["Invoice Number"].str.startswith("920-")]                                                                      

print("data_frame_in_set=>", data_frame_in_set)
data_frame_in_set.to_csv(output_file, index=False)
