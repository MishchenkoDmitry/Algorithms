import random

num = random.randint(0, 100)
i = 1

while i < 11:
    print("Попытка № " + f'{i}')
    num_user = int(input("Введите число от 0 до 100"))

    if num != num_user:
        if i == 10:
            print("Вы проиграли ...")
        else:
            if num > num_user:
                print("Ваше число меньше")
            else:
                print("Ваше число больше")
            i = i + 1
    else:
        print("Вы победили !!!")
        break
