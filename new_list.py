import math


s = [2, 4, 9, 16, 25]

# Через map
def sqrt(x):
    return math.sqrt(x)


qq = list(map(sqrt, s))
print(qq)

# В виде генератора списка
b = [math.sqrt(i) for i in [2, 4, 9, 16, 25]]
print(b)

# Через for
w = []
for i in s:
    w.append(math.sqrt(i))

print(w)