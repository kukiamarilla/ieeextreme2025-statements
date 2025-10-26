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
from collections import deque
import heapq

def solve(s):
    target = "112012"
    rs = len(s)//6
    res = [[] for i in range(rs)]
    asks = {
        "1": [i for i in range(rs)],
        "2": [],
        "0": [],
    }
    for i in range(len(s)):
        if len(asks[s[i]]) == 0:
            continue
        arr = heapq.heappop(asks[s[i]])
        res[arr].append(i)
        if len(res[arr]) < 6:
            heapq.heappush(asks[target[len(res[arr])]], arr)
    return res
t = get_number()

for i in range(t):
    s = get_word()
    res = solve(s) 
    for r in res:
        print(" ".join(map(lambda x: str(x+1), r)))