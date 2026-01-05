def two_sum(nums, target):
    dict = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in dict:
            return(dict[diff], i)
        else:
            dict[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))