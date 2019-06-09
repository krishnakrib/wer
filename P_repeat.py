h=int(input())
s=list(map(int,input().split()))
u=[]
for i in s:
    if(s.count(i)>1):
        u.append(i)
v=set(u)
if len(v)==0:
    print("unique")
else:
    print(*v)
