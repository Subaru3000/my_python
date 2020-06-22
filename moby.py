with open('moby1.txt','r') as file:
    s = file.readlines()

    trantab = str.maketrans({'-': None, ';': None, '.': None, ',': None})
    print(trantab)

    def ff(x):
        xx = x.translate(trantab)
        return xx

    ll = list(map(ff, s))

    def rr(ll):
        for i in range(0, len(ll)):
            q = ll[i].split()
            for j in range(0, len(q)):
                print(q[j])




    print(rr(ll))