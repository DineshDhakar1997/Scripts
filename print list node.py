# print list node
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
def pll(head):
    l=[]
    s=set()
    while head:
        l.append(head.val)
        if head in s:
                print('linked list cycle')
                nl=[head.val]
                c=head.next
                while  c!=head:
                    nl.append(c.val)
                    # print(c.val)
                    c=c.next
                print(nl)
                return l
        else:
            s.add(head)
        head=head.next
    print(l)