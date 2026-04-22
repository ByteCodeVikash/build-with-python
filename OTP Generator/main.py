import random
num=int(input("How much generate otp number: "))

otp=[]

for i in range(num):
    otp.append(random.randint(0,9))

result = int("".join(map(str,otp)))
print(result)    