import time
import math

def power(base, exp):
    if exp == 1:
        return base
    else:
        if exp%2 == 0:
            base1 = math.pow(power(base, exp/2), 2)
            if base1 > 1000000007:
                return base1%1000000007
            else:
                return base1
        else:
            base1 = base * math.pow(power(base, (exp - 1)/2), 2)
            if base1 > 1000000007:
                return base1%1000000007
            else:
                return base1
            
base = 2
exp = 200
start = time.time()
p = power(base, exp)
end = time.time()
print(p)
