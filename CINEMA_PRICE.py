"Фильм «Паразиты», "
"сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб."
"Фильм «1917»,"
"сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб."
"Фильм «Соник в кино», "
"сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб. "


a = input("Введите название фильма: ")
b = input("выбрать дату (сегодня, завтра): ")
c = input("выбрать время: ")
d = input("указать количество билетов: ")

def f1(x,z):
    if x=="Паразиты":
        if int(z)==12:
            pr=250
        elif int(z)==16:
            pr=350
        elif int(z)==20:
            pr=450
        return pr
    if x=="1917":
        if int(z)==10:
            pr=250
        elif int(z)==13:
            pr=350
        elif int(z)==16:
            pr=350
        return pr
    if x == "Соник в кино":
        if int(z) == 10:
            pr = 350
        elif int(z) == 14:
            pr = 450
        elif int(z) == 18:
            pr = 450
        return pr


qq=f1(a,c)


def price(y, w):
    qq = f1(a, c)
    if int(w) >= 20:
        xx = int(w)*0.8
    else:
        xx = int(w)
    if y == "завтра":
        return xx*qq*0.95
    else:
        return xx*qq


print(price(b,d))

