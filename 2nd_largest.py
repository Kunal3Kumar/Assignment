#WAP in python to print the 2nd largest number 
print("Enter 3 numbers")
x, y, z = int(input()), int(input()), int(input())
if x<y<z or z<y<x:
   print(y,"is the second smallest number")
elif y<z<x or x<z<y:
    print(z,"is the second smallest number")
else:
    print(x,"is the second smallest number")

