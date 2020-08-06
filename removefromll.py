# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    """
    Source: https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm

    Given a singly linked list of integers l and an integer k,
    remove all elements from list l that have a value equal to k.

    For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
    removeKFromList(l, k) = [1, 2, 4, 5];

    For l = [1000, 1000] and k = 1000, the output should be
    removeKFromList(l, k) = [];

    For l = [3, 1, 2, 3, 4, 5] and k = 6, the output should be
    removeKFromList(l, k) = [1, 2, 3, 4, 5];

    """

    prev = l
    head = prev

    if prev:

        current = prev.next

        while prev.value == k:
            if prev.next is None:
                return None
            prev.next = None
            prev = current
            current = current.next

        head = prev

        while current.next is not None:
            if current.value == k:
                prev.next = current.next
                current = prev.next
                continue

            prev = current
            current = current.next

        if current.value == k:
            prev.next = None

    return head
