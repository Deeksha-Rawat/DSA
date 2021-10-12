class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        if root is None:
            return True
        a = True
        b = True
        
        if root.right and root.left is None:
            return False
        if root.left and root.data < root.left.data:
            a = False
        if root.right and root.data < root.right.data:
            b= False
        if a and b and self.isHeap(root.left) and self.isHeap(root.right):
            return True
        return False
