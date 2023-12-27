#create linked list from array
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def cll(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        current.next = new_node
        current = new_node

    return head