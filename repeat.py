def f(string, n, c=0):
    if c < n:
        print(string * n)
        f(string, n,c=c+3)

f('laptop', 3)
