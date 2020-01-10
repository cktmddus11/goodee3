'''
Created on 2020. 1. 10.

@author: GDJ_19

    자바에서                               파이썬에서 
    entrySet() : 키, 값 둘다            items()
    keySet() : 키만                      keys()
    values()  : 값만                       values()

'''

foods = {"떡볶이" : "오뎅", "짜장면" : "단무지", "라면":"김치","맥주":"치킨"}
for i in foods.keys():
    print("%s => %s" %(i, foods[i]))
    
# 화면에서 음식을 입력받아서 궁합음식 출력하기
# 입력받은 음식값이 "종료" 인 경우 프로그램이 종료

while True:
    #  food = input(foods.keys()+"음식을 입력하세요 : ") +연산자때문에 에러남
    #<class 'dict_keys'> 타입이랑 문자열이니까
    # food= input(str(foods.keys())+"음식을 입력하세요 : ") => dict_keys(['떡볶이', '짜장면', '라면', '맥주'])음식을 입력하세요 : 
    food= input(str(list(foods.keys()))+"음식을 입력하세요 : ") # !!!
    if food == "종료":
        print("등록된 음식 갯수 : ", len(foods))#  print("등록된 음식 갯수 : "+str(len(foods))
        print("좋아하는 음식 : "+ str(list(foods.keys()))) #!!!
        print("궁합 음식 : "+str(list(foods.values()))) #!!!
        print("둘다 : "+str(list(foods.items())))
        print("둘다 중 하나 : "+str(list(foods.items())[-1]))
        break 
    if food in foods: # foods 의 key값이 존재?
        print(food,"=>",foods[food])
    else:
        print("등록된 음식이 아닙니다")    
        # 등록하는 프로그램 추가하기
        #  등록하시겠습니까? 여부를 물어서(Y)
        # Y면 등록
        check = input("좋아하는 음식으로 등록하시겠습니까?")
        if check == "y" or check == "Y":
            food2 = input("궁합음식을 입력하세요")
            foods[food] = food2 

  
    

    