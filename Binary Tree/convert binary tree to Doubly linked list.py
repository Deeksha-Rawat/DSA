def bToDLL(self,root):
        # do Code here
        a=[]
        self.inorder(root,a)
        n=len(a)
        
        head =  Node(a[0])
        curr= head
        for i in range(1,n):
            temp = Node(a[i])
            curr.right = temp
            temp.left = curr
            curr = curr.right
        return head 
