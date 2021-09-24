def levelOrder(self,root ):
  
  if root is None:
              return
          queue=[]
          ans=[]
          queue.append(root)
          while(len(queue)>0):
              ans.append(queue[0].data)
              s = queue.pop(0)
              if s.left:
                  queue.append(s.left)
              if s.right:
                  queue.append(s.right)
          return ans        
