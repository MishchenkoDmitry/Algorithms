n = int(input("Введите число n: "))

i = 1
sum = 0
sum1 = n * (n + 1) / 2

while i <= n:
    sum = sum + i
    i = i + 1

if sum == sum1:
    print("Утверждение верно")
else:
    print("Утверждение не верно")
