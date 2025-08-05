from collections import Counter
s1 = "ab"
s2 = "eidbaooo"
x = Counter(s1)

n = len(s1)

l,r = 0,n-1
k = False
while r<len(s2)+1:
    if Counter(s2[l:r+1]) == x:
        print(True)
        k = True
        break
    l+=1 
    r+=1

if not k:
    print(False)