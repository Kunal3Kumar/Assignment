units = int(input(" Please enter Number of Units you Consumed : "))

if(units > 1500):
    amount = units * 15

elif(units > 800 and units <= 1500):
    amount = units * 12

elif(units > 300 and units <= 800):
    amount = units * 9

else:
    units <= 300
    amount = units * 7

total = amount + 300
print("\nElectricity Bill = %.2f"  %total)