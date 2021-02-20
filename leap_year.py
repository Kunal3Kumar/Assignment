# WAP in python to check the given year is leap or not.
year=int(input("Enter Year: "))
if year % 4 == 0:
   if year % 100 == 0:
       if year % 400 == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
