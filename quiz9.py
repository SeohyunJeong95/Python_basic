class House:
    count = 0 
    def __init__(self,l):
        House.count += 1  # to call static variable
        self.l=l
    def detail(self):
        print("{} is the location".format(self.l))
h1 = House("songpa")
h2 = House("shibcheon")
h1.detail()
h2.detail()
print(h2.count)
# python 에서는 method overloading 자체를 지원하지 않는다. 
