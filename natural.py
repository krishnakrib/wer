n=int(input("enter the number"))
if n<0:
   print("enter the positive number")
else:
   sum=0
   while(n>0):
      sum+=n
      n-=1
   print("sum of the natural numbers are",sum)
