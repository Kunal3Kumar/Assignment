#prime number function
def prime(n):
    f = 0
    if n > 1:
        for i in range(2 ,n):
            if n % i == 0:
                f = 1
                break
    else:
        print('invalid input!!!!')

number = int(input("enter any number:"))
result = prime(number)
if result == 0:
    print("number is prime!!!")
else:
    print("number is not prime !!! ")