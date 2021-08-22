a="HELLO Python"
print(a[6:12])

b="AI 및 데이터 분석 기초"
print(b[5:15])

c='2019.09.01'
print(c[5:7])


number=input("주민번호 앞자리 입력: ")

y='20'+number[0:2]
m=number[2:4]
d=number[4:6]
age=2019-int(y)+1

print("당신은",y,"년에 태어났군요.")
print("당신의 생일은",m ,"월",d ,"일 이군요.")
print("당신은 올해",age ,"살 이군요.")


test_str="aaabbPythonbbbaa"
temp1=test_str.strip('a')
print(temp1)
