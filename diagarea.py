import math
dimensions = [[9,3],[8,6]]
maxa = []
area = []
maxi = -1
for i in dimensions:
    maxa.append(math.sqrt(i[0]*i[0]+(i[1]*i[1])))
    area.append(i[0]*i[1])

