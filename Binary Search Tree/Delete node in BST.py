def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return
        if key<root.val:
            root.left = self.deleteNode(root.left,key)
        elif key>root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root.right = None
                return temp
            if root.right is None:
                temp = root.left
                root.left = None
                return temp
            temp = self.minVal(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right,temp.val)
        return root
    def minVal(self,root):
        current = root
        while(current.left is not None):
            current = current.left
        return current
