def pattern():
    item = 9
    for row in range(1, 4):
        for col in range(1, 4):
            print(item, end = " ")
            item -= 1
        print('\n')
    
def pattern1():
    item = 2
    for row in range(1, 4):
        for col in range(1, 4):
            print(item, end =" ")
            item += 2
        print('\n')


if __name__ == "__main__":
    #pattern()
    pattern1()