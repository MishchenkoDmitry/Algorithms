quantity = int(input("Введите количество цифр: "))
num_search = int(input("Введите число для поиска: "))

q_num = 0
i = 1

while i <= quantity:
    num = input("Введите число № " + f'{i}' + ": ")
    for j in num:
        if int(j) == num_search:
            q_num = q_num + 1

    i = i + 1

print("Число повторялось: " + f'{q_num}' + " раз(а).")
