def count_list(lst):
    """Using recursion, return the length of a list.

    Test cases:

        >>> count_list([5, 6])
        2

        >>> count_list(['hi','bye','cat','dog','frog'])
        5

        >>> count_list(['yes'])
        1

        >>> count_list([])
        0
    """

    if lst == []:
        return 0

    lst.pop()
    return 1 + count_list(lst)


# doctest
if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
