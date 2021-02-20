#WAP to calculate and display the factorial of
#an inputted number.


num = int(input("enter the range for factorial: "))
f = 1

if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       f = f * i
   print("The factorial of",num,"is",f)
