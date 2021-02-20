sub1=int(input("Enter marks of the 1st subject: "))
sub2=int(input("Enter marks of the 2nd subject: "))
sub3=int(input("Enter marks of the 3rd subject: "))
sub4=int(input("Enter marks of the 4th subject: "))
sub5=int(input("Enter marks of the 5th subject: "))

avg=(sub1+sub2+sub3+sub4+sub4)/5

print("Avrage :",avg)

if(avg >= 90):
    print("Grade: O")
elif(avg >=80 and avg<90):
    print("Grade: E")
elif(avg>=70 and avg<80):
    print("Grade: A")
elif(avg>=60 and avg<70):
    print("Grade: B")
else:
    print("Grade: F")