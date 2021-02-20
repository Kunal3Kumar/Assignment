# file = open('test.txt','r')
# print(file.read())

# File = open('list.py','r+')
# str1 = file.read(10)
# print(str1)

# file = open('C:/Users/kkpan/Downloads/New folder/dbms.txt','r')
# print(file.read())

# file = open('test1.txt','w')
# file.write('this is new file\n')
# file.write('second line of this file')
# file.close()

# file = open('test1.txt','r')
# print(file.read())

file = open('test1.txt','a')
file.write('this line is for appending at the end')
file.close()

file = open('test1.txt','r')
print(file.read())