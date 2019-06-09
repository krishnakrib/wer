h=int(input())
s=list(map(int,input().split()))
u=[]
for i in range(h):
    for j in range(len(s)):
        if i==s[j]:
            if i not in u:
                u.append(i)
for x in u:
    print(x,end=' ')
