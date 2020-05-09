def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

s = 0

while True:
    t = input("Введите число или стоп: ")
    if t == "Стоп":
        print("Конец...","Сумма введенных чисел =",s)

        break
    elif is_number(t) == True:
        s = s + int(t)
    else:
        print("Повторите ввод числа")


