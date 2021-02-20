def tri_patt():
    print('Triangle')
    for row in range(1, 5):
        for col in range(1, row + 1):
            print('*', end=" ")
        print('\n')

def tripat():
  ran=int(input("Enter number:"))
  for i in range(1, ran+1):
    print("*" * i)
  print()

def tripat1():
    ran=int(input("Enter number:"))
    for i in range(1,ran+1):
      print(" "*(ran - i),"A"*i)
    print()


if __name__ == "__main__":
   # tri_patt()
   # tripat()
    tripat1()