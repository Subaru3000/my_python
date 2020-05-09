import random

number = random.randint(1, 4)

print(number)
x = int(input("Введите число: "))


if x == number:
    print("Победа")
elif x > number:
    print("Попробуйте еще раз")
    print("Число меньше введенного")
elif x < number:
    print("Попробуйте еще раз")
    print("Число больше введенного")