
def f(y):
    x = str(y)
    sum = 0
    for i in x:
        if int(i) % 2 != 0:
            sum = sum + int(i)**2
    return sum



print(f(1122222222222133))
