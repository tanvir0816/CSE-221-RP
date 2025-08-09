def power_modulo(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
    return result

def calculate_ab_mod(a, b):

    return power_modulo(a, b, 107)
a,b=map(int, input().split())
result = calculate_ab_mod(a, b)
print(result)

###### another solve#####

def solve(a,b,m):
    if b==0:
        return 1
    hal=solve(a,b//2,m)
    hal=(hal*hal)%m
    if b%2==0:
        return hal
    else:
        return (hal*(a%m))%m
a,b=map(int, input().split())
print(solve(a,b,107))