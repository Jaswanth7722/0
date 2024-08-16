def rightside_stars():
    a = int(input("enter the size = "))
    for j in range(0,a):
        for i in range(a-1-j):
            print(" ",end=' ')
        for k in range(0,j+1):
            print("*",end=' ')
        print(' ',end='\n')
def leftsidereverse_stars():
    b = int(input("enter the size = "))
    for j in range(0,b):
        for i in range(0,b):
            print("*",end=' ')
        b = b - 1
        print(" ",end='\n')
def leftside_stars():
    c = int(input("enter the size = "))
    for i in range(0,c):
        for j in range(0,i + 1):
            print("*",end=' ')
        print(" ",end='\n')
while True:
    print("Enter choice given below")
    print("1 . rightside_stars")
    print("2 . leftside_stars")
    print("3 . leftsidereverse_stars")
    print("4 . Quit")
    user_input= int(input("Enter choice : "))
    if user_input == 4:
        break
    elif user_input== 1:
        rightside_stars()
        print("\n")
    elif user_input == 2 :
        leftside_stars()
        print("\n")
    elif user_input == 3:
        leftsidereverse()
        print("\n")