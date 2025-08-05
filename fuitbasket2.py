fruits = [4,2,5]
baskets = [3,5,4]


for i,a in enumerate(fruits):
    for j,b in enumerate(baskets):
        if b>=a:
           fruits[i] = -1
           baskets[j] = -1
           break
count = sum(1 for i in fruits if i!= -1)
print(count)