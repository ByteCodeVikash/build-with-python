class PrimeNumberChecker:
      def __init__(self,num):
          self.num=num

      def show(self):
          if self.num<=1:
          	 print("Not prime")
          	 return

          for i in range(2,self.num):
              if self.num%i!=0:
                 print("not prime.")
                 return
          print("Prime number.")       
                  




num=int(input("Enter a number here: "))
a=PrimeNumberChecker(num)
a.show()