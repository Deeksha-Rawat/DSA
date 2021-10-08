# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        self.inorder(root,arr)
        return self.arrtoBST(arr)
        
    def inorder(self,root,arr):
        if root is None:
            return
       
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
        return arr 
    
    
    
    def arrtoBST(self,arr):
        n=len(arr)
        if arr is None:
            return
        while n:
            mid =n//2
            root = TreeNode(arr[mid])
            root.left = self.arrtoBST(arr[:mid])
            root.right = self.arrtoBST(arr[mid+1:])
            return root
    
    
    
