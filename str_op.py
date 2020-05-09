s = "У лукоморья 123 дуб зеленый 456"


#1
def f1(z):
    x = s.find(z)
    if x == -1:
        print("буква не встречается")
    else:
        print(x)


f1("я")

#2
def f2(s):
    print(s.count("у")+s.count("У"))


f2(s)

#3
def f3(s):
    if s.isalpha() == False:
        print(s.upper())


f3(s)

#4
def f4(s):
    if len(s) > 4:
        print(s.lower())


f4(s)

#5
def f5(s):
    print(s.replace(s[0], "o"))


f5(s)

