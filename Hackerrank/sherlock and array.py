def solve(a,n):
    rsum=0
    for i in range(1,n):
        rsum+=a[i]
    lsum=0
    i,j=0,1
    while j<n:
        rsum-=a[j]
        lsum+=a[i]
        if rsum==lsum:
            return 1
        j+=1
        i+=1
    return -1

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=sum(a[1:])
    if b==0:
        print("YES")
    else:
        s=solve(a,n)
        if s==1:
            print("YES")
        else:
            print("NO")
