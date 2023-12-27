    # Create linked list cycle  (cllc)


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
def cllc(arr, pos):
    if not arr:
        return None

    # Create the linked list without a cycle
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    # Find the node at the specified position
    cycle_node = head
    for i in range(position):
        cycle_node = cycle_node.next

    # Create the cycle by connecting the last node to the specified position
    current.next = cycle_node

    return head