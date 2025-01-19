# According to Eculidean algorithm for computing GCD
# gcd(10,15) = gcd(15-10,10) =gcd(5,10) = gcd(10-5, 5)=gcd(5,5) = 5

#gcd(18,12) = gcd(18-12,12) = gcd(6, 12) = gcd(12-6, 6) = gcd(6,6)
def gcd3(m,n):
    if (m<n):
        (m,n)=(n,m)
    if (m==n):
        return m
    else:
        return(gcd3((m-n),n))

# least common multiple
# Algorithm to compute LCM
def lcm2(m, n):
    # lcm of numbers is equal to multiplication of both numbers divided  by gcd
    return m * n // gcd3(m,n)

print(lcm2(18,12))