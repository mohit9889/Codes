def permutation(n,k):
    if k==0:
        for i in range(n):
            print(i+1,end=" ")
    elif n%(2*k)!=0:
        print("-1")
    else:
        for i in range(n):
            if(int(i/k)%2==0):
                print(i+k+1,end=" ")
            else:
                print(i-k+1,end=" ")

q=int(input())
for i in range(q):
    n,k=map(int, input().split())
    permutation(n,k)
