import calendar
def Calendar():
    year = int(input("Enter the year= "))
    month= int(input("Enter the month= "))
    print(calendar.month(year,month))
while True:
    print("Choose the options :")
    print("1. Calendar")
    print("2. Quit")
    print(" ")
    user_input= int(input("Enter the option = "))
    if user_input== 1:
        Calendar()
        print(" ")
        print(" ")
    if user_input==2:
        break