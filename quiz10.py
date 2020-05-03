chicken = 10 
waiting = 1 
class OutofStock(Exception):
    def __init__(self):
        self.msg = "out of stock sorry"
    def __str__(self):
        return self.msg
while(True):
    print("left chicken {} ".format(chicken))
    try:
        order = int(input("how many?"))
        if order > chicken:
            print("cannot make an order")
        elif order <=0 :
            raise ValueError
        else:
            print("{} <- waiting {} -> how many".format(waiting,chicken))
            waiting += 1
            chicken -= order
            try:
                if chicken == 0:
                    raise OutofStock
            except OutofStock as err:
                print(err)
                break
    except ValueError as err:
        print("invaild order",err)
    

