# 사이트로 비밀번호를 만들어 주는 프로그램을 작성하시오 
url_sentence= "http://naver.com"
my_str =url_sentence.replace("http://","")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str))+ str(my_str.count("e"))+"!"
print(password)
