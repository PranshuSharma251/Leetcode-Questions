s ="pwwkew"
maxy = 0
leny = 0
arr = []
r = 0
while r<len(s):
    if s[r]  not in arr:
        arr.append(s[r])
        leny+=1
    else:
        arr = []
        arr.append(s[r])
        maxy = max(maxy,leny)
        leny = 1
    r += 1

print(maxy)

