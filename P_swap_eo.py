h=input()
s=list(h)
s[::2],s[1::2]=s[1::2],s[::2]
print(' '.join(s))

