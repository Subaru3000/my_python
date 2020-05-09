s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
words = s.split()
print(words)

qq = list(filter((lambda x: x[0] != "м"), words))

print(qq)

