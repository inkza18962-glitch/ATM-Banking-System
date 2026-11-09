
menu = 0
money = 7000

while menu != 4:
    print("====================")
    print("WELCOME TO ATM")
    print("====================")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    print(money)

    try:
        menu = int(input("เลือกรายการ"))
    except ValueError:
        print("Invalid Input")
        continue

    if menu == 1:
        try:
            deposit = int(input("กรอกจำนวนเงินฝาก"))
        except ValueError:
            print("Invalid Input")
            continue

        if deposit <= 0:
            print("Invalid Amount")
        else:
            money = money + deposit
            print("Deposit Successful")

        print("ยอดคงเหลือปัจจุบัน", money)

    elif menu == 2:
        try:
            withdraw = int(input("กรอกจำนวนเงินถอน"))
        except ValueError:
            print("Invalid Input")
            continue

        if withdraw <= 0:
            print("Invalid Amount")
        elif withdraw > money:
            print("Insufficient Balance")
        else:
            money = money - withdraw
            print("Withdraw Successful")

        print("ยอดคงเหลือปัจจุบัน", money)

    elif menu == 3:
        print("Check Balance")
        print(money)

    elif menu == 4:
        print("Exit")

    else:
        print("Invalid Menu")

print("Good bye")
