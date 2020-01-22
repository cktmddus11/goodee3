'''
Created on 2020. 1. 22.

@author: GDJ_19
pandas 모듈을 이용하여 csv 파일을 읽고 쓰기
supplier_data.csv 다운받기
'''

import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out1.csv"

data_frame = pd.read_csv(input_file)
print(type(data_frame))
print(data_frame)
important_dates = ["1/20/14", "1/30/14"]
'''
    data_frame_in_set : Purchase Date 열의 값이 
                            "1/20/14", "1/30/14" 값에 속한 모든 컬럼 조회
                            
    loc : 행선택,  : 모든열
    isin : 포함하는.
'''
data_frame_in_set = \
data_frame.loc[data_frame["Purchase Date"].isin(important_dates), :]                                                                      
#           행중                    이 이름의 컬럼에  이 값으로 된거 가져와
# isin : 속해있는
print("data_frame_in_set=>", data_frame_in_set)
# to_csv : 선택된 데이터 csv 파일로 저장
data_frame_in_set.to_csv(output_file, index=False)
#                                     index=False 인덱스 제외 순수 데이터만 가져올때 