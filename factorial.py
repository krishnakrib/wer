num=7
fac=1
if num<0:
   print("fac does not exsists")
elif num==0:
   print("fac exsists")
else:
  for i in range (1,num+1):
    fac=fac*i
  print("The factorial of",num,"is",fac)
