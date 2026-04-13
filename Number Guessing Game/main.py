
import random
print("Game start choose number (1-100")
computer=random.randint(1, 100)
while True:

    
    num=int(input("Enter number here: "))
    if num< 1 or num>100:
        print("Invalid number.")
        continue
    if num==computer:
      print("you won!")
      break
    elif num>computer:
      print("try lower")
    else:
       print("try higher")       