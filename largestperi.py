nums = [1,2,1,10]

nums.sort()

for i in range(len(nums)-1,1,-1):
    if (nums[i-2]+nums[i-1])>nums[i]:
        print(nums[i]+nums[i-1]+nums[i-2])
        break
print(0)
