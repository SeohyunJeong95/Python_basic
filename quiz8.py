for i in range(1,51):
    with open(str(i)+"th.txt","w") as report: # w mode is 덮어쓰기 
        report.write("{} th report".format(i))