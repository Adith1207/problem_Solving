from collections import deque

class Node:
    def __init__(self,data):
        self.info = data
        self.left = None
        self.right = None



def topView(root):
    if root is None:
        return
    
    hd_node = dict()
    
    queue = deque()
    queue.append((root,0))

    min_hd = max_hd = 0

    while queue:
        node,hd = queue.popleft()

        if hd not in hd_node:
            hd_node[hd] = node.info
            min_hd = min(min_hd,hd)
            max_hd = max(max_hd,hd)
        
        if node.left:
            queue.append((node.left,hd-1))
        if node.right:
            queue.append((node.right,hd+1))
    
    for hd in range(min_hd,max_hd+1):
        print(hd_node[hd],end=' ')
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(6)

topView(root)