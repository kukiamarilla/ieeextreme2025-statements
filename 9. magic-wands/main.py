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

def swap(e):
    return "H" if e == "S" else "S"
    
def solve(n, k, s):
    s = list(s)
    c = 0
    for i in range(len(s)-k+1):
        if s[i] == "S":
            c += 1
            for j in range(k):
                s[i+j] = swap(s[i+j])
    return c if all(x == "H" for x in s ) else -1
    
t = get_number()
for i in range(t):
    n = get_number()
    k = get_number()
    s = get_word()
    print(solve(n, k, s))