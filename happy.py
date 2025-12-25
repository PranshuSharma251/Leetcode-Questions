happiness = [12,1,42]
k = 3
happiness.sort(reverse=True)
c = 0
for i in range(k):
    if happiness[i]-i>=0:
        c+= happiness[i]-i
    elif happiness[i]-i<0:
        c+=0
print(c)