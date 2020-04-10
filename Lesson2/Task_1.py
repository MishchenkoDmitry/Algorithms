# https://drive.google.com/file/d/1XrW5mm-A0cdLCuSlcKsvJ2_N8VB38nho/view?usp=sharing
while True:
    print("Для выхода нажмите 0")
    a = int(input("Введите число а:"))
    b = int(input("Введите число b:"))
    znak = input("Введите знак:")

    if znak == 0 or a == 0 or b == 0:
        break
    elif znak == "+":
        print("Сумма чисел =" + f'{a + b}')
    elif znak == "-":
        print("Разница чисел =" + f'{a - b}')
    elif znak == "*":
        print("Произведение чисел =" + f'{a * b}')
    elif znak == "/":
        print("Частное чисел =" + f'{a / b}')
