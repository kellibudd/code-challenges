def sum_list(nums):
    """Using recursion, return the sum of numbers in a list.
    
    Test cases:

        >>> sum_list([5, 5])
        10

        >>> sum_list([-5, 10, 4])
        9

        >>> sum_list([20])
        20

        >>> sum_list([])
        0
    """

    if nums == []:
        return 0

    return nums.pop() + sum_list(nums)


# doctest
if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
