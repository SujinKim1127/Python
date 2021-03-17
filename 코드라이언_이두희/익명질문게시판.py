# step 1
# def make_dolcelatte():
#     print("1. 얼음을 넣는다.")
#     print("2. 연유를 30ml 넣는다.")
#     print("3. 찬 우유를 넣는다.")
#     print("4. 에스프레소샷을 넣는다.")
#
# def make_blueberry_smoothie():
#     print("1. 블루베리 20g을 넣는다.")
#     print("2. 우유 30ml를 넣는다.")
#     print("3. 얼음을 넣는다.")
#     print("4. 믹서기에 간다.")
#
# def make_simple_latte():
#     print("1. 커피를 넣는다.")
#     print("2. ")
#     print("3. ")
#     print("4. ")
#
# make_simple_latte()
# make_blueberry_smoothie()

#step 4 5 6 7
total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)


total_list = []     # 비어있는 리스트 생성
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else :
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:  #질문 하나하나가 i에 저장
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer    # i 는 key값
print(total_list)
