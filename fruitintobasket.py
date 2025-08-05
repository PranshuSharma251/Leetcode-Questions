fruits = [1,2,1]
count = 0
for i in range(0,len(fruits)):
    coco = 0
    f = []
    for a in fruits[i:]:
        if a in f:
            coco += 1
        else:
            if len(f) == 2:
                break
            else:
                f.append(a)
                coco += 1
    count = max(count,coco)

print(count)