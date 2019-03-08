#начал учить питон, и это один из моих первых проектов))
import random
Number=random.randint(1,100)
user=-1
x=int(10)
print("игра создана юным программистом SoReNTo!\n\n\n\")
print("1)легкая(30 попыток)\n2)средняя(20 попыток)\n3)высокая(15 попыток)\n4)своя сложность(выбрать количество попыток)\n0)Выход\n")
b=int(input("Выбери сложность: "))
if (b==int(1)):
    x=30
elif (b==int(2)):
    x=20
elif (b==int(3)):
    x=15
elif (b==int(4)):
    x=(input("сколько будет попыток?: "))
    print("\n============")
elif (b==int(0)):
    print("Пока((")
    exit()
else:
    print("Такой сложности не существует)")
    input("нажми на любую кнопку, чтобы выйти:")
    exit()
    

        
while user!=Number:
    user=int(input("\nУгадай число от 1 до 100:"))
    if (x<2):
        print("-----------\n\n   Ты проиграл\n\n-----------")
        print("-----------\n\n  Число было: " + str(Number)) 
        break
    elif user > Number:
        x=x-1
        print("\n\n    Число должно быть меньше!\n\n=============\n")
        print("Попыток осталось:", x) 
    elif user < Number:
        x=x-1
        print("\n\n    Число должно быть больше!\n\n=============\n")
        print("Попыток осталось:", x)
    
    else:
        print("-----------\n\n   Ты выйграл\n\n-----------\n\n  число было: " + str(Number))
        break
    
