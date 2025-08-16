num = 66
k = str(num)
c = ''
for i,a in enumerate(k):
    if a == "6":
        c+='9'+k[i+1:]
        break
    else:
        c+= a
print(c)