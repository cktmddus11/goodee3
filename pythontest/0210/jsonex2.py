'''
Created on 2020. 2. 10.

@author: GDJ_19
json 내용에서 날짜와 과일의 가격을 화면에 출력하고 파일에 저장하기

'''
import json 
price = {
    "data" : "2020-02-10",
    "price" : {
        "Apple" : 800, 
        "Orange" : 1000,
        "Banana" : 500
    }
        
}

print(price["data"])
for p in price['price'].keys():
    print("%s => %s" %(p, price["price"][p]))
    
json.dump(price, open("json_output.json", "w", encoding="utf-8"))


