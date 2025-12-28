grid = [[3,2],[1,0]]
c = 0
for i in grid:
    for j in i:
        if j<0:
            c+=1
print(c)