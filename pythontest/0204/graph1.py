'''
Created on 2020. 2. 4.

@author: GDJ_19
그래프 그리기
'''

import matplotlib.pyplot as plt # pip install ggplot

plt.style.use("ggplot") #  그래프 그릴 떄 사용하는 모듈 ggplot
customers = ["JAVA", "JSP", "SPRING", "HADOOP", "PYTHON"] # 리스트
print(range(len(customers))) # 5
customers_index = range(len(customers)) # 0 ~ 4 인덱스 길이 5 
print(type(customers_index)) # range 타입
sale_amounts = [65, 90, 85, 60, 95] # 데이터 리스트 설정

fig = plt.figure() # 그래프 공간. 도화지
ax1 = fig.add_subplot(1, 1, 1) # 1행 1열 1번쨰 그래프
# 막대 그래프 그리기
ax1.bar(customers_index, sale_amounts, align="center", color="darkblue")
ax1.xaxis.set_ticks_position("bottom") # X축 설정
ax1.yaxis.set_ticks_position("left") # y축 설정

# X축 표시 설정
plt.xticks(customers_index, customers, rotation=0, fontsize="small")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")
# 이미지 저장하기
plt.savefig("bar_plot.png", dpi = 400, box_inches="title")
# 화면이 이미지 추가하기
plt.show()