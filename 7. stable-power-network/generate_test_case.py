import random
t = 10000
print(t)
for i in range(t):
    n = 2*10**5
    m = 3*10**5
    adj = []
    for j in range(m):
        u = random.randint(1, n)
        v = random.randint(1, n)
        while u == v:
            v = random.randint(1, n)
        w = random.randint(1, 10**9)
        r = random.randint(1, 10**9)
        adj.append((u, v, w, r))
    print(f"{n} {m}")
    for j in range(m):
        print(f"{adj[j][0]} {adj[j][1]} {adj[j][2]} {adj[j][3]}")