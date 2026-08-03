# 这是 LeetCode 的框架，你填中间
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    pass

nums = [3,2,4]
target = 6
print(twoSum(nums,target))