def Sieve(m,n):
    prime=[]
    if m==1:
        m+=1
    for i in range(m,n+1):
        if i not in prime:
            print(i)
            for j in range(i*i,n+1,i):
                prime.append(j)

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        m,n=map(int, input().split())
        Sieve(m,n)
