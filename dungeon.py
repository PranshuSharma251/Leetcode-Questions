energy = [-2,-3,-1]
k = 2
su = -99999999999999999999999999
for j in range(0,len(energy)):
    md = 0
    for i in range(j,len(energy),3):
        md += energy[i]
    su = max(md,su)
print(su)