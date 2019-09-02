def euclid_gcd(a, b):
    if a >= b:
        dividend = a
        divisor = b
    else:
        dividend = b
        divisor = a

    while(divisor != 0):
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend

def recursion_euclid_gcd(a, b):
    if a >= b:
        dividend = a
        divisor = b
    else:
        dividend = b
        divisor = a

    if divisor == 0:
        return dividend
    return recursion_euclid_gcd(divisor, dividend%divisor)
    

print(euclid_gcd(400, 124))
print(recursion_euclid_gcd(400, 124))
