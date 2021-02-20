# WAP to display factors of an inputted number.
num = int(input("Please Enter any Number: "))

val = 1


while (val <= num):
    if(num % val == 0):
        print("{0}".format())
    val = val + 1