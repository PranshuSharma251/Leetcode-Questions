s = "3902"
i = 0
while len(s)>2:
    x = ""
    for i in range(len(s)-1):
        x+= str((int(s[i]) + int(s[i+1]))%10)
    s = x

if s[0] == s[1] :
    print(True)