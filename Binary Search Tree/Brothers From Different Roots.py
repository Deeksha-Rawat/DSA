class Solution:
    def countPairs(self, root1, root2, x): 
        #code here.
        arr1=set()
        arr2=set()
        
        count=0
        self.inorder(root1,arr1)
        self.inorder(root2,arr2)
        for i in arr1:
            if (x-i) in arr2: 
                count+=1
        return count            
        
        
    def inorder(self,root,a):
        if root is None:
            return
        self.inorder(root.left,a)
        a.add(root.data)
        self.inorder(root.right,a)
