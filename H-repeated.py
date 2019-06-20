h=int(input())
s=input()
u=' '
for i in s:
    if i in u and i!=" ":
        print(int(i))
        break
    else:
        u+=i
if u==s:
    print("unique")
