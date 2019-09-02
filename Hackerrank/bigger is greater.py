def permutation(arr):
    n=len(arr)-1
    while n>0 and arr[n-1]>=arr[n]:
        n-=1
    if n<= 0:
        return False

    m=len(arr)-1
    while arr[m]<=arr[n-1]:
        m -= 1
    arr[n-1],arr[m] = arr[m],arr[n-1]
    arr[n:]=arr[len(arr)-1:n-1:-1]
    return True

t= int(input())
for i in range(t):
    s=list((input()))
    if permutation(s):
        print("".join(s))
    else:
        print("no answer")
