def rightView(self,root):
        
        # code here
        if root is None:
            return
    
        result=[]
        level = []
        queue = [root]
        while queue:
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(node.data)
            queue = level
            level = []
        return result 
