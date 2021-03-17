import random

#for x in range (30):
#    print(random.choice(["된장찌개","피자","치킨","떡볶이","라면","감자튀김"]))

# step 4
#import time

#while True:
#    print(random.choice(["된장찌개","피자","치킨","떡볶이","라면","감자튀김"]))
#    break
#    time.sleep(1)   

# step 5    
lunch = random.choice(["차돌된장찌개","매운떡볶이", "제육볶음"])
lunch="냉장고"
dinner = random.choice(["김밥", "쫄면", "돈까스"])
#print(lunch)

# STEP 6 Dictionary
information={"고향":"서울", "취미":"넷플릭스","좋아하는 음식":"라면"}
#print(information)
#print(information.get("취미"))

information={"특기":"퍼즐","사는 곳": "서울"}
#print(information.get("특기"))
#print(information.get("사는 곳"))

#step 7
information = {"고향":"서울", "취미":"넷플릭스","좋아하는 음식":"라면"}
foods = ["된장찌개", "피자", "제육볶음"]
#print(information.get("취미"))
information["특기"] = "퍼즐"
information["사는곳"] = "서울"
del information["좋아하는 음식"]  #삭제
#print(information)
#print(len(information))     #개수 출력
information.clear()         #전부 다 삭제
#print(information)
#print(foods[-2])     #맨 앞 정보 출력
foods.append("김밥")
#print(foods)
foods.remove("제육볶음")
#print(foods)

#step 8
foods=["떡볶이","순대","닭강정"]
#print(foods)
#for x in range(3):      # 0 1 2 까지
 #   print(foods[x])
#for x in foods:         # range 없음
 #   print(x)

information = {"고향":"서울", "취미":"넷플릭스","좋아하는 음식":"라면"}
#for x,y in information.items():
 #   print(x)    # 고향, 취미, 좋아하는 음식
  #  print(y)    # 서울, 넷플릭스, 라면

#step 9
foods = ["닭강정","떡볶이","꽈배기"]
foods_set1=set(foods)   # foods set 집합 형성
foods_set2=set(["닭강정","떡볶이","꽈배기"])
#print(foods_set1)
#print(foods_set2)

#step 10
foods = ["닭강정","떡볶이","꽈배기","닭강정"]
foods_set=set(foods)   # foods set 집합 형성

#print(foods)
#print(foods_set)    # 중복 알아서 제거

menu1 = set(["라면","짜장면","핫도그"])
menu2 = set(["라면","닭강정","꽈배기"])
menu3 = menu1 | menu2   # | : 합집합
menu4 = menu1 & menu2   # & : 교집합
menu5 = menu1 - menu2   # - : 차집합
#print(menu3)
#print(menu4)
#print(menu5)

#step 11 만약에
import random

food = random.choice(["짜장면", "칠리새우","탕수육"])
#print(food)
#if(food == "짜장면") :
  #  print("곱빼기로 주세요")
#else :
 #   print("그냥 주세요")
#print("주문 끝")

#step 12
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
#while True:
    #item=input("음식을 추가해주세요 : " )
    #lunch.append(item)  # 추가는 append!!
    #print(lunch)

#step 13
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    print(lunch)
    item=input("음식을 추가해주세요 : " )
    if (item == "q"):
        break
    else:   #입력값이 q가 아니면
        lunch.append(item)  # 추가는 append!!

print(lunch)

#step 14
#set_lunch = set(["떡볶이", "순대","오뎅","튀김"])
#item = "튀김"
#print(set_lunch - set([item]))     #문자열 아이템 --> 리스트 아이템
        # 차집합 연산 완료
#print(set_lunch)        # 튀김 안빠짐

#set_lunch = set_lunch - set([item])
#print(set_lunch)

#step 15
set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])     # 차집합 (삭제코드) [] = list

import time
print(set_lunch,"중에서 선택합니다.")
print("5")
time.sleep(1)   # 1초 세기
print("4")
time.sleep(1)   # 1초 세기
print("3")
time.sleep(1)   # 1초 세기
print("2")
time.sleep(1)   # 1초 세기
print("1")
time.sleep(1)   # 1초 세기

import random
print(random.choice(list(set_lunch))) # 집합 --> 리스트로 변경
