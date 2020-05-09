
names = ['John', 'Paul', 'George', 'Ringo']

a = list(filter((lambda x: len(x) == 4), names))
print(a)

