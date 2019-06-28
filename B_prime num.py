paw=int(input())
if(paw>0):
  for i in range(2,paw):
      if(paw%i)==0:
          print("no")
          break
  else:
      print("yes")
