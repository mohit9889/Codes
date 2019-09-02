def solve(a,k,n):
    count=0
    a.sort()
    l=0
    r=0
    while r<n:
        if a[r]-a[l]==k:
            count+=1
            l+=1
            r+=1
        elif a[r]-a[l]>k:
            l+=1
        else:
            r+=1
    print(count)

n,k=map(int, input().split())
a=list(map(int, input().split()))
solve(a,k,n)
