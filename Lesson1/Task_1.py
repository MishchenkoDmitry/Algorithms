#https://drive.google.com/file/d/1DPwP4-jORx1_hjUVCf0e01YAn0HAvjb0/view?usp=sharing

num = int(input("Введите трехзначное число: "))

a= num % 10

num = num // int(10)
b = num % int(10)
c = num // int(10)

summa_number = a +b + c
composition_number = a * b * c

print("Сумма чисел = " + f'{summa_number}')
print("Произведение чисел = " + f'{composition_number}')