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
    q = get_number()
    
    types = [] 
    
    for i in range(n):
        types.append(get_number())
        
    adj = [[] for i in range(n)]
    for i in range(n-1):
        u = get_number() - 1
        v = get_number() - 1
        adj[u].append(v)
        adj[v].append(u)
        
    parent = [None]*n
    dist = [float('inf')]*n
    height = [0] * n
    visited = set()
    
    def preset(u, v, h):
        if types[u] == 1:
            dist[u] = 0
        height[u] = h
        parent[u] = v
        visited.add(u)
        child_dists = []
        for k in adj[u]:
            if k not in visited:
                child_dists.append(preset(k, u, h+1)+1)
        cd = float('inf')
        if len(child_dists)> 0:
            cd = min(child_dists)
        final_dist = min(dist[u], cd)
        dist[u] = final_dist
        return final_dist
    preset(0, None, 0)
    
    def parent_dist(u):
        for v in adj[u]:
            if v != parent[u]:
                dist[v] = min(dist[v], dist[u]+1)
                parent_dist(v)
    parent_dist(0)

    def lca(u, v):
        min_dist = float('inf')
        while u != v:
            if height[u] > height[v]:
                min_dist = min(min_dist, dist[u])
                u = parent[u]
            else:
                min_dist = min(min_dist, dist[v])
                v = parent[v]
        min_dist = min(min_dist, dist[u])
        return min_dist
    
    for i in range(q):
        u = get_number() - 1
        v = get_number() - 1
        print(lca(u, v))
        

solve()