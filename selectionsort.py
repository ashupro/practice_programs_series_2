nums=[4,7,9,3,5,6]
def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if (nums[j]<nums[minpos]):
                minpos=j

        temp=nums[minpos]
        nums[minpos]=nums[i]
        nums[i]=temp

sort(nums)
print(nums)