nums = [1,3,-1,-3,5,3,6,7]
k = 3
res,l= [],0
for r in range(k-1,len(nums)):
    res.append(max(nums[l:r+1]))
    l+=1
print(res)