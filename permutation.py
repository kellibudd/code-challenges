def permute(nums):
    """
    Source: https://leetcode.com/problems/permutations/submissions/
    """

    print("*" * 5)
    if len(nums) <= 1:
        print("hi")
        return [nums]

    length = len(nums)

    combinations = []

    for i in range(length):
        current = nums[i]
        print(current)
        nums_copy = nums.copy()
        nums_copy.pop(i)
        smaller_lists = permute(nums_copy)
        print("smaller list: ", smaller_lists)

        for lst in smaller_lists:
            lst.insert(0, current)
            print("list: ", lst)
            combinations.append(lst)

    return combinations
