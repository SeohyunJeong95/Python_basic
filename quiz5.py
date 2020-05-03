from random import *
ids = [1,2,3,4,5,6,7,8,9,10]
print("당첨자 발표")
shuffle(ids)
print("치킨 당첨자:"+str(sample(ids,1)))
print("커피 당첨자:"+str(sample(ids,3)))

#users = range(1,21) 1부터 20 까지의 숫자를 생성 

