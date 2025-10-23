values = [1,2,3]

values.sort()
su = 0
for i in range(len(values)-2):
    su += values[0] * values[1] * values[i+2]

print(su)