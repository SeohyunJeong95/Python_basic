# Data type 
print(5)
print(-10)
print(3.14)
print(1000)

#arithmetic 
print(5+3)

# string type 
print('Happy 풍선')
print('A'*10)

#boolean 
print(5>10)
print(5<10)
print(True)
print(not True)

# variable
name = "happy"
animal = "dog"
age = 4
hobby = "walk"
is_adult = age >= 3

print("우리집 "+ animal + "의 이름은 "+ name+"에요")
#print("나이는 "+str(age), "살이며")
print("나이",age,"살이며") # + 대신에 ',' 사용 가능하고, 하나의 띄어쓰기를 포함한다. 형변환은 알아서 됌
print("어른일까요? "+ str(is_adult))

#arithmatic 
# and 도 가능하고 & , or 도 가능하고 |
print(2**3) # 2^3 
print(10//3) # 10/3
print(2==3)
print(2!=3) 
print(not (2==3))

# library function 
print(abs(-5))
print(pow(4,2))
print(max(2,5))
print(round(3.222)) # 반올림 

# math library
from math import * # import syntax
print(floor(4.99))  # 내림
print(ceil(4.99)) # 올림 
print(sqrt(16)) # root, float 형으로 나온다. 

# random generator
from random import *
print(random()) # 0 ~ 1.0
print(random()*10) # 0 ~ 10
print(int(random()*10)) # 0 ~ 10
print(int(random()*10)+1) # 1 ~ 10
print(int(random()*10)+1) # 1 ~ 10
print(int(random()*10)+1) # 1 ~ 10
print(int(random()*45)+1) # 1 ~ 45

# randrange
print(randrange(1,46)) # 1 ~ 45(마지막은 미만이기 때문에 46)

# randint 
print(randint(1,45)) # including 1 and 45. 

# 문자열 sentence는 단지 var name 이다.
sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워오"
print(sentence2)

sentence3 ="""
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

a = """
나는 서현이고,
파이썬 하기시러오
"""
print(a)

# slicing 
jumin = "950704-1234567"
print("성별:",jumin[7])
print("year:",jumin[0:2]) # 2번째 직전값까지.즉, 0,1
print("DOB:",jumin[:6]) # 처음부처 6 직전까지 
print("last digit:",jumin[7:14])
print("last digit:",jumin[7:]) # 시작 digit 부터 끝 digit 까지 
print("last digit:",jumin[-7:])# 맨뒤에서 마이너스 7 부터 끝까지 

# 문자열 처리 함수 
python = "Python is Amazing"
print(python.lower()) # lower case
print(python.upper()) # upper case
print(python[0].isupper()) # indexing 하는 거 잘보세욤
print(len(python))
print(python.replace("Python","Java")) # python을 찾아서 java로 바뀌어서 출력 

index = python.index("n") # 첫번째 occurence,  없으면 runtime error and quit  
print(index) 

index = python.index("n",index + 1) # 앞에 있는 5 라는 것에서 하나를 더한 다음 위치 .. 그러니까 다음 위치 
print(index)  

index = python.find("JAVA") # 첫번째 occurence 
print(index) # 원하는 값이 포함 되지 않을 땐 -1 반환 

count = python.count("n")
print(count)

# 문자열 포맷 _방법 1
print("나는 %d살입니다." % 20)
print("나는 %s살입니다." % "파이썬")
print("나는 %c살입니다." % "A")

print("%s %s." % ("blue","red"))

# 방법 2
print("나는 {}살입니다 {}." .format("blue",20))
print("나는 {1}살입니다 {0}." .format("blue",20))

# 방법 3
print("나는 {age}살입니다 {color}." .format(age= 20, color ="pink"))

# 방법 4
age = 24 
color = "blue"
print(f"나는 {age}살입니다 {color}")  # 변수 사용하기 

# 탈출 문자 
print("백문이 불여일견\n 백견이 불여일타") # \n
print("저는 \"나도 코딩\" 입니다.") # \n
print("C:\\Users\\ellie\\Desktop\\Python\\Python>")

# \r 커서를 맨 앞으로 
print("red Apple\rPine")

# \b : 한글자 삭제 backspace
#\t : tab

# list 
subway = [10,20,30]
print(subway)
subway = ["a","b","c"]
print(subway)
print(subway.index("a")) # indexat
subway.append("d") # append to the last
print(subway)
print(len(subway))
print(subway.count("a"))
subway.insert(1,"seo")
print(subway)

print(subway.pop())
print(subway)

# 빈리스트 선언 
arr =[3,3,5,6,7,1,2,9]
arr.sort()
arr.reverse()
# arr.clear()
print(arr)

#다양한 자료형과 함께 사용할수있다.
#리스트 확장
arr.extend(subway)
print(arr)

#dictionary 
cabinet= {3:"John",100:"Kevin"} # key:value, key could be any type 

# all return value
print(cabinet[3])
#print(cabinet[5]) # force quit 
print(cabinet.get(3)) 
print(cabinet.get(5)) # NONE

print(cabinet.get(5,"available")) # key가 지정이 안되어있으면 문자열 반환
print(3 in cabinet) # 3 이라는 key가 dictionary에 있느냐 return boolean 

# string type key dictionary 
cabinet= {"A-20":"John","B-20":"Kevin"} 
print(cabinet)
cabinet["C-20"] = "Ellie"
print(cabinet)

cabinet["C-20"] = "San" # update the value if key is already taken 
print(cabinet)

# del
del cabinet["C-20"]
print(cabinet)

# print keys 
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

#clear
cabinet.clear() 

# TUPLE
# 가로 없이 선언도 가능함 
menu  = ("water","happy") # final array, cannot modify the contents of the list
print(menu[0])
print(menu[1])
# menu[0]= "www" error occurs 

# name ="John"
# age = 20 
# hobby = "coding"
# print(name,age, hobby)

# 한번에 선언 
n, a, h = "John",20,"coding"
print(n,a, h)

# Set 
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3,3}
java = {"a","b","c"}
python= {"a","d","e"}

print(java & python)
print(java.intersection())

# 자료 구조의 변경 
# memu ={"커피","우유"}
# list(menu) # 집합 형태로 바꿈 

#if  and or 
weather = "rain"
if weather == "rain" or weather =="snow":
    print("take your umbella")
elif weather == "dust":
    print("take your mask")
else:
    print("nothing to prepare")

# loop
for i in [0,1,2,3,4]:
    print("대기번호: {}".format(i))

for i in range(5): # 0,1,2,3,4
    print("대기번호: {}".format(i))
for i in range(1,6): # 1,2,3,4,5
    print("대기번호: {}".format(i))

startbucks = ["a","b","c"]

for i in startbucks:
    print("coffe is ready: {}".format(i))
for i in range(0,3): # indexing
    print("ready: {}".format(startbucks[i]))
print("dddddd")

#while
target = 1
unknown = 0
# while unknown != target:
#     print("{} your coffee is ready".format("tori"))
#     unknown = int(input("what is your id?:"))

#continue and break 
for i in range(0,6): # 0,1,2,3,4,5
    if i == 3 or i==2:
        continue
    else:
        print("read book {}".format(i)) 
print("out of loop")
for i in range(0,6): # 0,1,2,3,4,5
    if i == 3:
        break
    else:
        print("read book {}".format(i)) 

absent =[2,5]
nobook = [7,10]
for student in range(1,11):
    if student in absent: # in the list of "absent "
        continue
    if student in nobook:
        print("follow me {}".format(student))
        break
    print("go read {} ".format(student))

# studnents = [1,2,3,4,5]
# print(studnents)
# students = [i+100 for i in studnents]
# print(students)

students = ["aaa","aaaaaa","bbbbb"]
# students = [len(i) for i in students]
# print(students)
# for i in range(0,len(students)):
#     students[i] = len(students[i])
# print(students)

# all upper case 
students = [i.upper() for i in students]
print(students)
