def two_sum(nums, target):

    for idx, num in enumerate(nums):
        for i in range(len(nums) - 1):
            summed = num + nums[i]
            if summed == target:
                print(num)
                print(nums[i])
                return summed
        print(nums.pop(idx))


two_sum([2, 10, 7, 11, 15], 22)
