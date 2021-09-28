def leftView(self,root):
        
        # code here
        if root is None:
            return
    
        result=[]
        level = []
        queue = [root]
        while queue:
            for node in queue:
              
              if node.right:
                    level.append(node.right)
              if node.left:
                  level.append(node.left)
                
            result.append(node.data)
            queue = level
            level = []
        return result 
