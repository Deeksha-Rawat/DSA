def reverse(S):
  stack = []
  for i in S:
      stack.append(i)
  a=''
  while len(stack):
      a+=stack.pop()
  return a    
