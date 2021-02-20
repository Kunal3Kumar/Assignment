#WAP to input a number and check whether the number is 2 digit number or not.
number = float(input("Enter your number: "))

if number >= 10 and number < 100:
    print("the number is 2 digit number",number)
else:
    print("not 2 digit number:",number)

number2 = input("enter a number:")
l = len(number2)
print(l)