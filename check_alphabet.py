# write a Python program to check whether the entered value is an Alphabet or not.
ch = input("Enter a character: ")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch, "is an Alphabet")
else:
    print(ch, "is not an Alphabet")

#both programe is same
ch = input("Enter a charater")
if (ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='O' or ch=='o' or ch=='I' or ch=='i' or ch=='U' or ch=='u'):
    print (ch,"is a Vowel")
else:
    print (ch,"is a Constant")