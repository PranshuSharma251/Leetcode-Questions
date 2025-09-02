points = [[6,2],[4,4],[2,6]]
c = 0
for i in range(0,len(points)):
    for j in range(i+1,len(points)):
        if (points[i][0] <= points[j][0] and points[i][1] >= points[j][1]) or (points[i][0] >= points[j][0] and points[i][1] <= points[j][1]):
            l = 0
            for r in points:
                if (points[i][0]<r[0]<points[j][0] or points[i][0]>r[0]>points[j][0]) and (points[i][1]<r[1]<points[j][1] or points[i][1]>r[1]>points[j][1]):
                    l = 1
                    break
            if l == 0:
                c+=1

print(c)

