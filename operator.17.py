a = float(input("Enter 1st number :"))

b = float(input("Enter 2nd number :"))

op = input("Enter operator [+ - * / %] :")

if op=='+':
    result = a + b

elif op =='-':
    result = a - b

elif op=='*':
    result = a * b

elif op=='/':
    result = a / b

else:
    print("Invalid operator!!")

print(a,op,b,'=',result)