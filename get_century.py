import math


def centuryFromYear(year):
    """
    Source: Codesignal
    Given a year, return the century it is in. The first century spans
    from the year 1 up to and including the year 100, the second - from
    the year 101 up to and including the year 200, etc.

    Test case:
    >>> centuryFromYear(1905)
    20
    >>> centuryFromYear(45)
    1
    >>> centuryFromYear(1700)
    17
    """

    base_century = math.floor((year / 100))
    year = (year / 100) % 1

    if year > 0.00:
        year = 1
    else:
        year = 0

    return base_century + year


# doctest
if __name__ == "__main__":
    import doctest

result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
