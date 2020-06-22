with open('text.txt') as file, open('text_update.txt', 'w') as writer:
    s = file.readlines()
    print(s)
    a = []
    def f(x):
        y = str(x)+" "+s[x-1]
        return y



    for i in range(1, len(s)+1):
        a.append(f(i))


    print(a)
    writer.writelines(a)