import random
while True:
    Number=random.randint(1,100)
    user=-1
    x=int(10)
    print("1)легкая(20 попыток)\n2)средняя(15 попыток)\n3)высокая(10 попыток)\n4)своя сложность(выбрать количество попыток)\n0)Выход\n")
    b=int(input("Выбери сложность: "))
    if (b==int(1)):
        x=20
    elif (b==int(2)):
        x=15
    elif (b==int(3)):
        x=10
    elif (b==int(4)):
        x=(int(input("сколько будет попыток?: ")))
        print("\n============")
    elif (b==int(0)):
        input("нажми на любую клавишу, чтобы выйти:")
        exit()
    else:
        print("Такой сложности не существует)")
        input("нажми на любую клавишу, чтобы выйти:")
        exit()   
    while user!=Number:
        user=int(input("\nУгадай число от 1 до 100:"))
        if x < int(2):
            print("-----------\n\n   Ты проиграл\n\n-----------")
            print("-----------\n\n  Число было: " + str(Number)) 
            break
        elif user > Number:
            x=x-1
            print("\n\n    Число должно быть меньше!\n\n=============\n")
            print('попыток осталось:', x) 
        elif user < Number:
            x=x-1
            print("\n\n    Число должно быть больше!\n\n=============\n")
            print('попыток осталось:', x)
        elif user == "exit" == "quit" == "q":
            input("нажми на любую клавишу, чтобы выйти:")
        elif UnicodeError:
            continue
        else:
            print(11*"=""\n\n   Ты выйграл\n\n"(11*"=")("\n\n  число было: ") + str(Number))
            input("нажми любую клавишу")
            break
