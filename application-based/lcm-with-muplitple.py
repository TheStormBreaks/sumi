# least common multiple
# Algorithm to compute LCM
def lcm1(m, n):
    # lcm can not be greater than m*n and smaller than max(m,n)
    for i in range(max(m, n), m*n +1):
        # if a number is divisible by both m and n
        if i%m == 0 and i%n == 0: 
            return i # return lcm

print(lcm1(6,12))