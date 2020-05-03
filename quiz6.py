from random import *
num = 0 
for customer in range(0,50):
    time = randrange(5,51)
    if ( 5<= time <= 15 ):
       num +=1
       print("[O] {}st customer time {}".format(customer,time))
    else:
        print("[] {}st customer time {}".format(customer,time))
print("{} is total customers".format(num))
