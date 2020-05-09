import math

w = float(input("Введите число: "))

def f(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1

print(f(w))
