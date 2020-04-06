a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if ((b > a) and (a > c)) or ((c > a) and (a > b)):
    print("Среднее число а: " + f'{a}')
elif ((a > b) and (b > c)) or ((c > b) and (b > a)):
    print("Среднее число b: " + f'{b}')
else:
    print("Среднее число c: " + f'{c}')
