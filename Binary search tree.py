def minValue(root):
    ##Your code here
    if root is None:
        return -1
    if root.left is not None:
        return minValue(root.left)
    else:
        return root.data
