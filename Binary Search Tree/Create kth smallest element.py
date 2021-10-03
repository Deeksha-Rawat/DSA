def KthSmallestElement(self, root, k): 
        #code here.
        arr=[]
        self.bsttoarray(root,arr)
        if k<=len(arr):
            return arr[k-1]
        else:
            return -1
        
        
def bsttoarray(self,root,arr):
    if root is None:
        return None
    self.bsttoarray(root.left,arr)
    arr.append(root.data)
    self.bsttoarray(root.right,arr)
