# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return 
    while head != slow:
        head = head.next
        slow = slow.next
    return head
