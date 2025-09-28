from collections import Counter
s = "aeiaeia"
t = Counter(s)
t = t.most_common()
v = 'aeiou'
su,j,i,k= 0,0,0,0
while i< len(t) and (j<1 or k<1):
    if t[i][0] in v and j<1:
        j+= 1
        su += t[i][1]
    elif t[i][0] not in v and k<1:
        k+=1
        su += t[i][1]
    i+=1
print(su)