year = int(input("Введите год: "))

if year % 4 == 0:
    if year % 100 !=0:
        print("Год высокосный")
    else:
        print("Год обычный")
else:
    if year % 400 == 0:
        print("Год высокосный")
    else:
        print("Год обычный")