num=int(input("Enter a number here: "))
temp=num

sum=0

n=len(str(num))

while temp>0:
	digit=temp%10
	sum+=digit**n
	temp=temp//10

if sum==num:
	print("it is armstrong number.")
else:
    print("it is not armstrong.")	



