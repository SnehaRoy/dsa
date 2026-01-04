def contains_duplicate(nums):
    seen = set()
    for i in range(0, len(nums)):
        if nums[i] in seen:
            return True
        else:
            seen.add(nums[i])
    return False

nums = [1,2,3,10]
print(contains_duplicate(nums))