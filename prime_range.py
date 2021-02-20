#WAP to print prime numbers between 55 and 180.
print("Enter lower and upper number:")
l,u = int(input()), int(input())

for num in range(l,u + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end =" ")