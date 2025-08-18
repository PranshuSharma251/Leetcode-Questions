nums = [-1,0,3,5,9,12]
target = 2

l,r = 0,len(nums)-1


while l<=r:
    md = l+((r-1)//2)
    if target < nums[md]:
        r = md - 1
    elif target > nums[md]:
        l = md + 1
    else:
        print(md)
print(-1)