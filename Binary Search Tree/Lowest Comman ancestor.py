class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LCA(root,n1,n2):
    if root is None:
        return 
    if root.data > n1 and root.data > n2:
        return LCA(root.left,n1,n2)
    if root.data < n1 and root.data < n2:
        return LCA(root.right,n1,n2)
    return root            


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
 

t = LCA(root,10,14)
print(t.data)




###################33333
def LCA(root,n1,n2):
    while root:
        if root.data > n1 and root.data>n2:
            root = root.left         
        if root.data < n1 and root.data < n2:
            root = root.right      
        else:
            break
    return root
