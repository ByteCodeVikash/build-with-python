def PalindromeChecker(string):
            Reversstring=string[::-1]


            if string==Reversstring:
                print("this is Palindrome string")
            else:
                print("this is not Palindrome string")


string=input("Enter string here: ")
PalindromeChecker(string)                