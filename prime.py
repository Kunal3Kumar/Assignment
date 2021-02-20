# WAP in python to check the given number is prime or not.
num=int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("given num is not a prime number:",num)
            break
        else:
            print("given num is prime:",num)
else:
    print("given num is prime:",num)