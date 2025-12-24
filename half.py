nums = [10,10,3,7,6]
c = 0
for i in range(len(nums)-1):
    if ((sum(nums[0:i+1])-sum(nums[i+1:len(nums)]))%2) == 0:
        c+=1
print(c)