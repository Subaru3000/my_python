def ph(kod,time):
    if kod == 381:
        return 18*time
    elif kod==343:
        return 15*time
    elif kod== 473:
        return 13*time
    elif kod==485:
        return 11*time



print(ph(473,10))