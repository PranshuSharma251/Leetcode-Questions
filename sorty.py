apple = [1,3,2]
capacity = [4,3,1,5,2]
capacity.sort(reverse=True)
z = sum(apple)
c = 0
for i in capacity:
    if i < z:
        c+=1
        z-=i
    elif i>z:
        c+=1
        print(c)
        break
    elif i==z:
        c+=1
        print(c)
        break