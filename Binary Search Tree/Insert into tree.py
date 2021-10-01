if root is None:
    return TreeNode(val)
if val<root.val:
    root.left = self.insertIntoBST(root.left,val)
if val>root.val:
    root.right = self.insertIntoBST(root.right,val)
return root    
