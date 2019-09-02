#for checking primality Navia approach of O(N)
def checkPrime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count+=1
    if count==1:
        print("Yes")
    else:
        print("No")

#for checking primality in O(sqrt(N))
def isPrime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i+=1
    return True
        
'''
Sieve of Eratosthenes:
You can use the Sieve of Eratosthenes to find all the prime numbers
that are less than or equal to a given number N or to find out whether
a number is a prime number.
The basic idea behind the Sieve of Eratosthenes is that at each iteration
one prime number is picked up and all its multiples are eliminated. After
the elimination process is complete, all the unmarked numbers that remain are prime.

Pseudo code:
1.Mark all the numbers as prime numbers except 1
2.Traverse over each prime numbers smaller than sqrt(N)
3.For each prime number, mark its multiples as composite numbers
4.Numbers, which are not the multiples of any number, will remain marked as
  prime number and others will change to composite numbers.

Time Complexity=O(NloglogN)
'''
def sieve(n):
    prime=[True]*(n+1)
    prime[0]=prime[1]=False
    i = 2
    while i*i <= n:
        if prime[i]==True:
            j=i*i
            while j <= n:
                prime[j]=False
                j += i
        i += 1
    for i in range(len(prime)):
        if prime[i]==True:
            print(i)

#Modification of Sieve of Eratosthenes for fast factorization in sqrt(N)
def factorize(n):
    result = []
    i=2
    while i*i <= n:
        while n%i == 0:
            result.append(i)
            n /= i
        i += 1
    if result != 1:
        result.append(int(n))
    print(*result, sep=" ")
    
factorize(10)
