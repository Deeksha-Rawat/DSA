def inorder(root):
  inorder(root.left)
  print(root.data,end=" ")
  inorder(root.right)


def mirror(root):
  if root == None:
    return
  mirror(root.left)
  mirror(root.right)
  root.left,root.right=root.right,root.left
  

mirror(root)
print(inorder(root))
  
