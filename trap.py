from collections import Counter
from math import comb
y = []
for i in points:
    y.append(i[1])
v = Counter(y)
a = v.values()
xs = [comb(v,2) for v in a]
s1 = sum(xs)
s2 = sum(x*x for x in xs)
s = (s1*s1 - s2)//2
print(s)
