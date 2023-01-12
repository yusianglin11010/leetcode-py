def getIntersectionNode(headA, headB):
    p1, p2 = headA, headB
    len_a, len_b = 0, 0
    while p1:
        len_a += 1
        p1 = p1.next
    while p2:
        len_b += 1
        p2 = p2.next
    if len_a > len_b:
        for _ in range(len_a-len_b):
            headA = headA.next
    else:
        for _ in range(len_b-len_a):
            headB = headB.next
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1