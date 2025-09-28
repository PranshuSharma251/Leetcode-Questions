text = "hello world"
brokenLetters = "ad"
s = text.split()
counter = 0
for i in s:
    for j in i:
        if j in brokenLetters:
            counter += 1
            break
print(len(s)-counter)