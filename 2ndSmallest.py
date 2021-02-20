n1=int(input("Enter the first no.:"))
n2=int(input("Enter the second no.:"))
n3=int(input("Enter the third no.:"))
if(n1<n2 and n1<n3):
    smallest=n1
elif(n2<n1 and n2<n3):
    smallest=n2
else:
    smallest=n3

if(n1>smallest and n1<n3):
    secsmallest=n1
elif(n2>smallest and n2<n3):
    secsmallest=n2
else:
    secsmallest=n3

print(secsmallest)
