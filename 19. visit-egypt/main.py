# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy
t = get_number()
tc = []
for i in range(t):
    n = get_number()
    m = get_number()
    a = get_number()
    tc.append((n, m, a))
n, m, a = max(tc)

def ways(n):
    mod = 10**9+7
    n *= 53
    n *= 100
    n //= 25
    coins = [25, 50, 100, 500, 1000, 2000, 5000, 10000, 20000]
    coins = [x//25 for x in coins]
    w = [0 for i in range(n+1)]
    w[0] = 1
    for i in range(1, n+1):
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                w[i] += w[i - coins[j]]
                w[i] %= mod
    return w
w = ways(n)

def solve(n, m, a):
    global w
    if m == a:
        return "TIE"
    n *= 53
    n *= 100
    n //= 25
    m = abs(m - w[n])
    a = abs(a - w[n])
    if m == a:
        return "NONE"
    if m < a:
        return "Mikel"
    return "Andrew"
        

for i in range(t):
    n, m, a = tc[i]
    print(solve(n, m, a))