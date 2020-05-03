# function
# def open_account():
#     print("new account is opened")
# def deposit(blanace, add):
#     print("deposit function is called")
#     print("{} is bal ".format(blanace+add))
#     return blanace+ add
# blanace = deposit(10,11)

# def profile(name,age=17,main_lan="python"):
#     print("name {}, age {}, main_lan {}"\
#         .format(name,age,main_lan))
# profile("kevin",20,"java")
# profile("seohyun")
# def profile(name,age,*language):
#     print("name {}, age {}"\
#         .format(name,age))
#     for lang in language:
#         print(lang,end=" ")
# profile("kevin",20,"java")

# standard io 
# print("java","python", sep=" vs ") # seperate -> sep 
# print("java","python", end="?") # end="?" 마지막줄에 ? 넣고 그냥 이어주기 
# print("what is your type?")
# stdout , stderr ???
# scores ={"math":70,"eng":100}
# for sub,sco in scores.items():
#     print(sub,sco)

# standard input
# ans = input("whatever you want: ") # ans is string 
# print("your input is "+ans)

# file standard io
# score_file = open("score.txt","w",encoding="utf8")
# print("math: 0",file=score_file)
# print("eng: 100",file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("science: 80")
# score_file.write("\ncoding: 80")

# score_file = open("score.txt","r")
# print(score_file.read())
# score_file.close()

score_file = open("score.txt","r")
# print(score_file.readline(),end="") # one line by one 그리고 커서 다음줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

# lines = score_file.readlines() # all line to list type
# for line in lines:
#     print(line,end="")
# score_file.close()

# pickle
import pickle 
#profile_file = open("profile_file.pickle","wb")
# profile ={"name":"kevin","age":20,"hobby":["baseball","coding"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile data type -> profile_file
# profile_file.close()

# profile_file = open("profile_file.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with
# with open("profile_file.pickle","rb") as profile:
#     print(pickle.load(profile))

with open("study.txt","w") as study_file:
    study_file.write("studying python right now")
with open("study.txt","r") as study_file:
    print(study_file.read())