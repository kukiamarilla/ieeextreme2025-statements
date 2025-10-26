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

def solve():
    n = get_number()
    k = get_number()
    c = []
    for i in range(n-1):
        c.append(get_number())
    exists = set([0])
    def query(a, b):
        lk = k
        if a != 0:
            lk -= c[a-1]
        if b != 0:
            lk -= c[b-1]
        if lk < 0:
            return False
        def path(lk):
            if lk in exists:
                return True
            for i in range(len(c)):
                if lk-c[i] < 0:
                    continue
                if path(lk-2*c[i]):
                    exists.add(lk)
                    return True
            return False
        return path(lk)
    
    q = get_number()
    for i in range(q):
        a = get_number()
        b = get_number()
        res = query(a,b)
        if res:
            print("Yes")
        else:
            print("No")
    
        
solve()