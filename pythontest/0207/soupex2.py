'''
Created on 2020. 2. 7.

@author: GDJ_19
soupex2.py : 크롤링 예제

'''
from bs4 import BeautifulSoup

import urllib.request as req
url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# res : url 에 전달된 데이터. soup 의 분석 대상 데이터
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser") #BeautifulSoup 객체화
title = soup.find("title").string # title 태그의 내용
wf = soup.find("wf").string # 이 안에 있는 거 xml태그로 <![CDATA[로 되어있는데
#                                                                   파싱이 불가능한 순수 문자열 이기 때문에 <br>태그가
#                                                           있어도 그대로 나옴
print(title)
print(wf)
