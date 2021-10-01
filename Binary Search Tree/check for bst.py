def isBST(root,min_allowed,max_allowed):
        if root is None:
            return True
        if(min_allowed is not None and root.data <= min_allowed.data):
            return False
        if(max_allowed is not None and root.data >= max_allowed.data):
            return False
    
        leftvalid = isBST(root.left,min_allowed,root)
        rightvalid = isBST(root.right,root,max_allowed) 
        return leftvalid and rightvalid 



#geeks for geeks practice solution#######333
def isBST(self,root,min_allowed=None,max_allowed=None):
        if root is None:
            return True
        if(min_allowed is not None and root.data <= min_allowed.data):
            return False
        if(max_allowed is not None and root.data >= max_allowed.data):
            return False
    
        leftvalid = self.isBST(root.left,min_allowed,root)
        rightvalid = self.isBST(root.right,root,max_allowed) 
        return leftvalid and rightvalid  
