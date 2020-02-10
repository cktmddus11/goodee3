'''
Created on 2020. 2. 10.

@author: GDJ_19
yaml 예제
json 과 비슷한 문서 저장 방식. 2001년에 생성됨
'''
 
import yaml #pip install pyYAML
yaml_str = """
    Date : 2019-01-03
    PriceList : 
        -
            item_id : 1000
            name : banana
            color : yellow
            price : 800
        -
            item_id : 1001
            name : orange
            color : orange
            price : 1400
        - 
            item_id : 1002
            name : Apple
            color : red
            price : 2400
            
"""
# 하이픈(-) -> 리스트 형태로 들감?
# yaml 문서를 파이썬 자료형 (Dictionary)로 변경
data = yaml.load(yaml_str, Loader = yaml.FullLoader)
print(type(data))
print(data["Date"], "과일 가격")
for item in data["PriceList"]:
    print(item["name"], item["price"])
    
customer = [
        {"name" : "Inseong", "age":"24", "gender":"man"},
        {"name" : "Kildong", "age":"22", "gender":"man"},
        {"name" : "ChunHang", "age":"20", "gender":"woman"},
        {"name" : "HangDan", "age":"25", "gender":"woman"}
]    
# 파이썬 데이터(List) 를 yaml 문서양식으로 변경하기
yaml_str = yaml.dump(customer)
print(type(yaml_str))
print(yaml_str)
    
    
    
# yaml 문서를 파이썬 자료형(List) 로 변경
data = yaml.load(yaml_str, Loader=yaml.FullLoader)
for d in data:
    print(d["name"], d["age"], d["gender"])    
    
    
    
    
    
    
    