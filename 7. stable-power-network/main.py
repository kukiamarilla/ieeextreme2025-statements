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

visited = []
def solve(n, edges):
    global visited
    adj = [dict() for i in range(n)]
    for edge in edges:
        u, v, W, R = edge
        u -= 1
        v -= 1
        u, v = sorted((u, v))
        params = (R, W)
        if v not in adj[u]:
            adj[u][v] = params
            adj[v][u] = params
        adj[u][v] = min(adj[u][v], params)
        adj[v][u] = min(adj[v][u], params)
        
    sh = dijkstra1(adj)
    maxR = sh[n-1]
    nadj = [dict() for i in range(n)]
    visited = [False for i in range(n)]
    nadj = dfs(n-1, adj, sh, nadj)
    sh = dijkstra2(nadj)
    minT = sh[n-1]
    print(f"{maxR} {minT}")
    
def dfs(u, adj, sh, nadj):
    global visited
    visited[u] = True
    for v in adj[u].keys():
        R, W = adj[u][v]
        if max(sh[u], R) == sh[v]:
            nadj[u][v] = (R, W)
            nadj[v][u] = (R, W)
        if not visited[v]:
            dfs(v, adj, sh, nadj)
    return nadj
            
def dijkstra1(adj):
    start = 0
    sh = [float('inf') for i in range(len(adj))]
    sh[0] = 0
    visited = [False for i in range(len(adj))]
    q = deque([start])
    while len(q) > 0:
        u = q.popleft()
        if visited[u]:
            continue
        for v in adj[u].keys():
            params = adj[u][v]
            L = params[0]
            sh[v] = min(sh[v], max(sh[u], L))
            if visited[v]:
                continue
            q.append(v)
        visited[u] = True
    return sh

def dijkstra2(adj):
    start = 0
    sh = [float('inf') for i in range(len(adj))]
    sh[0] = 0
    visited = [False for i in range(len(adj))]
    q = deque([start])
    while len(q) > 0:
        u = q.popleft()
        if visited[u]:
            continue
        for v in adj[u].keys():
            params = adj[u][v]
            L = params[1]
            sh[v] = min(sh[v], sh[u] + L)
            if visited[v]:
                continue
            q.append(v)
        visited[u] = True
    return sh


t = get_number()
for i in range(t):
    n = get_number() 
    m = get_number()
    adj = []
    for j in range(m):
        edge = (
            get_number(),
            get_number(),
            get_number(),
            get_number()
        )
        adj.append(edge)
    solve(n, adj)


        
