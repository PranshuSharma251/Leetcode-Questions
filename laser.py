bank = ["011001","000000","010100","001000"]
laserB = []
for i in bank:
    c = i.count('1')
    if c!=0:
        laserB.append(c)
f = 0
for i in range(len(laserB)-1):
    f += (laserB[i]*laserB[i+1])
print(f)