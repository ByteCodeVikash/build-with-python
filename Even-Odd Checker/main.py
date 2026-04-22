class EvenOddChecker:
      def __init__(self,num):
          self.num=num

      def show(self):
          if self.num%2==0:
             print(self.num,"is Even")
          else:
             print(self.num,"is odd")


num=int(input("Enter a number here: ")) 

a=EvenOddChecker(num)
a.show()               