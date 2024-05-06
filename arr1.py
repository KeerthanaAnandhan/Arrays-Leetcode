def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

nums = [2, 7, 11, 15]  # Example array
target = 9             # Example target
result = two_sum(nums, target)
if result:
    print("Indices:", result)
else:
    print("No two sum solution")
