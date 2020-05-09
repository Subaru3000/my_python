import random


s = ['самовар', 'весна', 'лето']
a = random.choice(s)
print(a)
b = random.choice(a)
print(b)
c = a.replace(b, "?")
print(c)

d = input("Введите букву: ")

if d == b:
    print("Победа")
    print("Слово:", a)
else:
    print("Это провал...", "В следующий раз у вас получится.", "Попробуйте еще раз")