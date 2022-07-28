class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

def has_cycle(head: ListNode) -> ListNode:
    """Floyd's Cycle Finding Algorithm"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None

def node_where_cycle_begins(head: ListNode, meeting_point: ListNode) -> ListNode:
    """meeting_point is the Node where the cycle is detected,
    returned by the function has_cycle(head) above"""
    if head and meeting_point:
        slow = head
        fast = meeting_point
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None