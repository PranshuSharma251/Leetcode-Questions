nums = [0,1,1,1,0,1,1,0,1]

current = []
count = 0

for i in nums:
    if i == 1:
        current.append(1)
    elif i== 0:
        count = max(len(current),count)    
        