def counting(N):
    count=0
    while(N>0):
        N = N//10
        count = count + 1
    return count
N=int(input(" "))
count = counting(N)
print("num=",count)
