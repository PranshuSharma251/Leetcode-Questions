s = "lEetcOde"
vov = ['A','E','I','O','U','a','e','i','o','u']
vo = []
poopy = ''
for i in s:
    if i in vov:
        vo.append(i)
vo.sort()
for i in s:
    if i in vov:
        poopy += vo.pop(0)
    else:
        poopy+=i
print(poopy)