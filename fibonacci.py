#WAP in python to print fibonacci searis
Last_term = int(input("How many terms? "))

x = 0
y = 1
count = 0

if Last_term == 1:
   print("Fibonacci searis upto",Last_term,":")
   print(x)
else:
   print("Fibonacci searis:")
   while count < Last_term:
       print(x)
       z = x + y
       
       x = y
       y = z
       count += 1
