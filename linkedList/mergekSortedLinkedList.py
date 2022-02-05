from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return 0


from queue import PriorityQueue

q = PriorityQueue()

q.put((1, ListNode(2)))
q.put((2, ListNode(3)))
q.put((3, ListNode(4)))

node = q.get()
print(node[1].val)