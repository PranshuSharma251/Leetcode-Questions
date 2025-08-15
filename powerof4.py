n = 1
i = 0
if n >0:
    while i>=0:
        print(n)
        if 4**i == n:
            print(True)
            break
        elif 4**i > n:
            print(False)
            break
        else:
            i+=1
else:
    print(False)