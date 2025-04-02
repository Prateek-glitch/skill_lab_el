class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_kth_from_end(head, k):
    first = head
    second = head

    # Move the first pointer k steps ahead
    for _ in range(k):
        if first is None:
            # k is greater than the length of the list
            return None
        first = first.next

    # Move both pointers until the first pointer reaches the end
    while first:
        first = first.next
        second = second.next

    return second.value
