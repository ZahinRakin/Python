from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while lists.next


    def sort(self, l1, l2):
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail = l1 if not l2 else l2
        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]

solution = Solution()
merged_list = solution.mergeKLists(lists)

while merged_list:
    print(merged_list, end=' ')
    merged_list = merged_list.next
