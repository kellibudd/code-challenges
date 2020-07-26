def binary_search(val):
    """Using binary search, find value in range 1-100. Return number of guesses.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7

    """

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    floor = 0
    ceiling = 100

    for i in range(floor, ceiling + 1):
        # print("i: ", i)
        # print("floor: ", floor)
        # print("ceiling: ", ceiling)

        guess = ((ceiling - floor) // 2) + floor
        # print("guess: ", guess)
        num_guesses += 1
        # print("num_guesses: ", num_guesses)
        if val == guess:
            return num_guesses
        elif val < guess:
            ceiling = guess
        else:
            floor = guess + 1

    return num_guesses


# doctest
if __name__ == "__main__":
    import doctest

result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
