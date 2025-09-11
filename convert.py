n = 10108
x = str(n)
z = []
v = ''
for i,a in enumerate(x):
    print(i,a)
    if a == '0':
        v+= '1'
    elif a!='0' and i!= 0:
        v+= '0'

v = int(v)
z.append(v)
z.append(n-v)
print(z)