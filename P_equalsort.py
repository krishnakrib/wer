h=int(input())
s=list(map(int,input().split()))
u=[]
for i in range(0,h):
    if(int(s[i]==i)):
        u.append(s[i])
if(u==[]):
    print("-1")
else:
    u.sort()
    for j in range(0,len(u)):
        print(u[j],end=" ")
