unit = int(input("Enter your unit: "))
if unit <= 300:
    bill = 300
elif unit >= 301 and unit <= 800:
    bill = 300*7+(unit-300)*9
elif unit >= 801 and unit <= 1500:
    bill = 300*7+(unit-300)*12
else:
    bill = 300*7+(unit-300)*15

if bill < 300 :
    bill = 300
     
print("Your total bill is: ",bill)