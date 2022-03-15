from collections import defaultdict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return node
    if not node.neighbors:
        return Node(1)
    
    nodes = [None for _ in range(101)]
    res = Node(node.val)
    nodes[1] = res
    
    seen = defaultdict(bool)
    seen[1] = True
    stack = [node]
    while stack:
        cur = stack.pop(0)
        for neighbor in cur.neighbors:
            if not nodes[neighbor.val]:
                nodes[neighbor.val] = Node(neighbor.val)
            
            if not seen[neighbor.val]:
                stack.append(neighbor)
                seen[neighbor.val] = True
            
            c = nodes[cur.val]
            c.neighbors.append(nodes[neighbor.val])
    return nodes[1]
        