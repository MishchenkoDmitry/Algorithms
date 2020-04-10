num = int(input("Введите число"))
even = ""
noteven = ""
for i in num:
    if i % 2 == 0:
        even = even + i
    else:
        noteven = noteven + i

print("Четные числа: " + f'{even}')
print("Нечетные числа: " + f'{noteven}')
