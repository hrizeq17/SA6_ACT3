def find_max(nums, compare):
    max_num = nums[0]
    for num in nums:
        max_num = compare(max_num, num)
    return max_num

numbers = [100, 200, 100, 500, 3000]
greater = lambda x, y: x if x > y else y

max_number = find_max(numbers, greater)

print("Maximum number:", max_number)
