"""
Source: Interview Cake

Question: I opened up a dictionary to a page in the middle and started flipping 
through, looking for words I didn't know. I put each word I didn't
 know at increasing indices in a huge list I created in memory. 
When I reached the end of the dictionary, I started from the
 beginning and did the same thing until I reached the page I started at.
Now I have a list of words that are mostly alphabetical, except 
they start somewhere in the middle of the alphabet, reach the end, 
and then start from the beginning of the alphabet. In other words, 
this is an alphabetically ordered list that has been "rotated". 
Write a function for finding the index of the "rotation point.
"""


def find_rotation_pt(words_lst):
    """Given a list of words, write a function
    for finding the index of the "rotation point.

    Test case:

    >>> words = ['ptolemaic','retrograde','supplant','asymptote', 'babka']
    >>> find_rotation_pt(words)
    3
    """

    i = 1

    for i, word in enumerate(words_lst):
        if words_lst[i - 1][0] < words_lst[i][0]:
            continue
        else:
            return i


# doctest
if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
