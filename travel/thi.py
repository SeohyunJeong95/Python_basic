class thi:
    def detail(self):
        print("thi package")

if __name__ =="__main__":
    print("thi 모듈을 직접 실행 ")
    print("이 문장은 모듈을 직접 실행할 때만 실행")
    trip_to = thi()
    trip_to.detail()
else:
    print("외부")