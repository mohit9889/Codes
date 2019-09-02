import time
PHI = 1.6180339
f = [ 0, 1, 1, 2, 3, 5 ] 

#Program 1
def naive_fib(n):
    if n<=1:
        return n
    else:
        f=naive_fib(n-1)+naive_fib(n-2)
        return f

#Program 2
def memo_fib(n,memo):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    else:
        f=memo_fib(n-1,memo)+memo_fib(n-2,memo)
        memo[n]=f
        #print(memo)
        return f
#Program 3
def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

def fib(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F
    
#Program 4 
def fib2 ( n ): 
    if n < 6: 
        return f[n] 
    t = 5
    fn = 5
    while t < n: 
        fn = round(fn * PHI) 
        t+=1
    return fn 

#main()
start=time.time()
n=100000
print(fib(n))
#memo={}
#for i in range(n):
    #print(memo_fib(i,memo))
    #print(naive_fib(i))
print("%s sec" %(time.time()-start))
    
