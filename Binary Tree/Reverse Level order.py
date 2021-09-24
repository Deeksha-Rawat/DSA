def reverseLevelOrder(root):
    # code here
    ans=deque()
    queue=deque()
    if root is None:
        return
    queue.append(root)
    while(queue):
        node = queue.popleft()
        ans.appendleft(node.data)
        
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
            
    return ans    
