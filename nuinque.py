n = 5
res = []
if n == 1:
    res.append(0)
elif n%2 == 0:
    for i in range(1,int(n/2)+1):
        res.append(-i)
        res.append(i)
elif n%2 != 0:
    res.append(0)
    for i in range(1,int(n//2)+1):
        res.append(-i)
        res.append(i)
res.sort()
print(res)