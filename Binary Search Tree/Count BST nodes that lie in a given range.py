def getCount(root,low,high):
  
  if root is None:
          return 0
      if root.data==low and root.data==high:
          return 1
      count=0
      if root.data>=low and root.data<=high:
          return (1+getCount(root.right,low,high)+getCount(root.left,low,high))
      elif root.data<low:
          return getCount(root.right,low,high)

      else:
          return getCount(root.left,low,high)
