def addition(a,b):
	return a+b

def substration(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
    	print("Cannot divide by zero.")
    return a/b


while True:
      print("\n1.add 2.sub 3.multi 4.divide 5.exit")
      choice=int(input("Enter your choice(1-4): "))
      if choice==5:
      	 print("Program exited")
         break

      a=int(input("Enter first number here: "))
      b=int(input("Enter second number here: "))

      if choice==1:
         print(addition(a,b)) 
      elif choice==2:
         print(substration(a,b))
      elif choice==3:
         print(multiplication(a,b))
      elif choice==4:
         print(division(a,b))
      else:
         print("Invalid choice")                      	

