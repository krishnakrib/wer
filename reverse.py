n=int(input())
count=0
while n>0:
    m=n%10
    count=count*10+m
    n=n//10
print(" " , count)
