n = 1
res = ""
for i in range(35, 128):
    res = res + chr(i)
    if n % 10 == 0:
        print(res)
        res = ""
    n = n + 1

print(res)
