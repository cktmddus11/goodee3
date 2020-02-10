'''
Created on 2020. 2. 10.

@author: GDJ_19
'''
import json
import os.path
import urllib.request as req
url = "https://api.github.com/repositories"
savename = "repo.json" # url 에서 전달된 json파일을 저장
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
# json.load : 해당 파일의 내용을 json 형태로 파싱하기
items = json.load(open(savename, "r", encoding="utf-8"))
print(type(items)) # 리스트타입, 리스트 안은 딕셔너리로 ㅌ 
for item in items:
    print(item["name"]+"-"+item["owner"]["login"])
#json.dump : json 형태의 데이터를 파일로 저장
json.dump(items, open("json_output.json", "w", encoding="utf-8"))