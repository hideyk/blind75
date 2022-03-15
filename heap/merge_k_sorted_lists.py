from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from heapq import heapify, heappop
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for node in lists:
        while node:
            heap.append(node.val)
            node = node.next
    
    heapify(heap)

    head = ListNode()
    res = head
    while heap:
        head.next = ListNode(heappop(heap))
        head = head.next
        
    return res.next


from queue import PriorityQueue
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = res = ListNode()
    pq = PriorityQueue()

    for l in lists:
        if l:
            pq.put((l.val, l))
    
    while not pq.empty():
        v, ln = pq.get()
        head.next = ListNode(v)
        head = head.next
        ln = ln.next
        if ln:
            pq.put((ln.val, ln))

    return res.next


def main():
    pq = PriorityQueue()
    pq.put((2, ListNode(2)))
    pq.put((3, ListNode(2)))
    pq.put((4, ListNode(2)))
    print(pq.get())
    
if __name__ == "__main__":
    main()