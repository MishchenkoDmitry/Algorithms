print("Введите координаты первой точки")
x1 = float(input("X1: "))
y1 = float(input("Y1: "))
print("Введите координаты второй точки")
x2 = float(input("X2: "))
y2 = float(input("Y1: "))

k = (y1 - y2)/(x1 - x2)
b = y2 - k * x2

print("Уравнение прямого вида у = " + f'{k}' + "x + " + f'{b}')

