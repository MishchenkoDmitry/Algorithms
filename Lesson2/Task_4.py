def my_func(m, n, sum):
    if n == 0:
        return f'{sum}'
    else:
        m = m / 2 * (-1)
        n = n - 1
        sum = sum + m

        return my_func(m, n, sum)


n = int(input("Введите количество элементов: "))

m = 1
sum = 1

print("Сумма = " + f'{my_func(m, n - 1, sum)}')
