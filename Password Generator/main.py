import random

num=int(input("how much password length: "))
password=""
i=1
chars = "abcABC123@#"

while i<=num:
       password=password+random.choice(chars)
       	
       i+=1


print(password)       