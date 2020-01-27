nums=[6,9,3,7,8,2]
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if (nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

sort(nums)
print(nums)