def kthLargest(self,root, k):
        #your code here
        arr=[]
        self.bsttoarray(root,arr)
        ans = arr[len(arr)-k]
        return ans
def bsttoarray(self,root,arr):
    if root is None:
        return None
    self.bsttoarray(root.left,arr)
    arr.append(root.data)
    self.bsttoarray(root.right,arr)
