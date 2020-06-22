s = "( ) { [ ] ( ) { } }"

def fff(s):
    x = s.split()
    x = list(dict.fromkeys(x))
    su = 0
    for i in range(len(x)):
        su = su + s.count(x[i])

    if su % 2 == 0:
        print("Симметричны")
    else:
        print("Несимметричны")


fff(s)

sp = "( ( ) "
fff(sp)