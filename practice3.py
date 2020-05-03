# # # # # class Parent:
# # # # #     def __init__(self):
# # # # #         self.val = "Parent" 
# # # # #     def show(self):
# # # # #         print(self.val)
# # # # # class Child(Parent):
# # # # #     def __init__(self):
# # # # #         Parent.__init__(self)
# # # # #         self.val = "Child"
# # # # #     def show(self):
# # # # #         print("inside of Child")
# # # # #         print(self.val)

# # # # # obj1 = Child()
# # # # # obj1.show()

# # # # # building 
# # # # # error handling 
# # # # # try:
# # # # #     print("{}".format(2/0))
# # # # # # except ValueError:
# # # # # #     print("error has occured")
# # # # # # except ZeroDivisionError as error:
# # # # # #     print(error)
# # # # # except Exception as err:
# # # # #     print(err)

# # # # # class BigNumberError(Exception):
# # # # #     def __init__(self,msg):
# # # # #         self.msg = msg
# # # # #     def __str__(self):
# # # # #         return self.msg
# # # # # try:
# # # # #     print("one calculator")
# # # # #     num1 = 30
# # # # #     num2 = 2
# # # # #     if num1 >= 10 or num2 >= 10:
# # # # #         raise BigNumberError("number type is {} {}".format(num1,num2)) # error raise 하는 법 
# # # # #     print("{}".format(num1/num2))
# # # # # except BigNumberError as err:
# # # # #     print(err)

# # # # # module - encapsulate reusable code .. something like lib
# # # # # import module as mod
# # # # # # module.price(3)
# # # # # # module.price_morning(3)
# # # # # mod.price_morning(30)

# # # # # from module import *
# # # # # price(3)
# # # # # price_morning(5)

# # # # from module import price_morning
# # # # price_morning(3)

# # # # import travel.thi
# # # # trip_to = travel.thi.thi()
# # # # trip_to.detail()

# # # # from travel.thi import thi
# # # # trip_to = travel.thi.thi()
# # # # # trip_to.detail()

# # # # from travel import *
# # # # trip_to = thi.thi()
# # # # trip_to.detail()

# # # import inspect 
# # # import random
# # # print(inspect.getfile(random))

# # # pip install 
# # from bs4 import BeautifulSoup
# # soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# # print(soup.prettify())

# #input 
# # lan = input("which lan?")
# # print("{}".format(lan))

# # dir - 무슨 변수와 함수를 가지고 있는지를 표시해준다 
# # print(dir())
# # import random # 외장 함수
# # print(dir())

# # list = [1,2,3]
# # print(dir(list))

# # 내장함수 - 파이썬에서 이미 import 되어 있는 함수들 
# # 외장함수 - import 해줘야 하는것

# # glob - ls 같은거
# # import glob
# # print(glob.glob("*.py"))

# # os 
# import os
# print(os.getcwd())
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("exist")
#     os.rmdir(folder)
# else:
#     os.makedirs(folder)
#     print(folder,"made")

# time
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d "))