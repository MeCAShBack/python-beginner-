try:
    User1 = int(input("Введите первое число "))
    operator = input("ВВедите оператор")
    User2 = int(input("Введите второе число"))
    if operator == "+":
        print(User1 + User2)
    elif operator == "-":
        print(User1 - User2)
    elif operator == "*":
        print(User1 * User2)
    elif operator == "/":
        if User2 == 0:
            print("на ноль делить нельзя")
        else:
            print(User1 / User2)

    else:
        print("неизвестное число")
except:
