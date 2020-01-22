'''
Created on 2020. 1. 22.

@author: GDJ_19

pandas 모듈을 사용하여 column 조회하기
'''
import pandas as pd
input_file = "supplier_data.csv"
output_file = "pandas_out3.csv"
df = pd.read_csv(input_file)
df_col = df.iloc[:, [0, 3]] # 0번 열과 3번열 조회
#              : =>    모든행의 저 열만 가져와
print("=======df.iloc[:, [0, 3]]==")
print(df_col)
df_col=df.iloc[0:4, 0:3] 
#                    행0123,   열012 
print("=======df.iloc[0:4, 0:3]====")
print(df_col)
df_col.to_csv(output_file, index=False)


print("==========")
# 모든 행의 Invoice Number, Cost 컬럼 조회
#           iloc : index 행접근
df_col = df.iloc[:, [1, 3]]
print(df_col)
#          loc : 이름 행 접근
df_col = df.loc[:, ['Invoice Number', 'Cost']]
print(df_col)

df_col = df.loc[df["Invoice Number"].str.startswith("920-"), ["Invoice Number", "Cost"]]
#      Invoice Number 이 920으로 시작하는 행에서                 이 컬럼 값을 가져와
print(df_col)