def height(self, root):
        
        if root is None:
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
          
          
######

def height(self,right):
  if root is None:
    return 0
  return 1+max(self.height(root.left),self.height(root.right))
