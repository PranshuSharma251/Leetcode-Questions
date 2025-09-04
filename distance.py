x = 2
y = 5
z = 6

dif1 = max(x,z) - min(x,z)
dif2 = max(y,z) - min(y,z)
if dif1>dif2:
    return(1)
elif dif2>dif1:
    return(2)
elif dif1 == dif2:
    return(0)