#WAP to print the grade 
s1 = float(input("Enter marks for subject 1 :"))
s2 = float(input("Enter marks for subject 2 :"))
s3 = float(input("Enter marks for subject 3 :"))
s4 = float(input("Enter marks for subject 4 :"))

total = s1 + s2 + s3 + s4 
avg = total / 4
print('Average marks:',avg)
if avg >= 90:
    print("O")
elif avg >= 80:
    print("E")
elif avg >= 70:
    print("A")
elif avg >= 60:
    print("B")
elif avg >= 50:
    print("C")
else:
    print("you are fail")
