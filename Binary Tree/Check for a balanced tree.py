if root is None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh)>1:
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            
            return True
    
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
