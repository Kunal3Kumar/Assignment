#WAP to print the following series
#  Enter the range: 20
# 1 3 5 7 9 11 13 15 17 19  

num =  int(input("enter the num:"))
for i in range(1, num + 1,2):
    print (i, end=",")