from heapq import heappush, heappop

def delivery_route_optimizer(n, edges, warehouse, customers, charging_stations, battery_capacity):
    
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    
    def dijkstra(src):
        dist = [float('inf')] * n
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, u = heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heappush(heap, (dist[v], v))
        return dist

    all_dist = [dijkstra(i) for i in range(n)]

   
    target_mask = (1 << len(customers)) - 1
    customer_index = {c: i for i, c in enumerate(customers)}

    dp = {}
    heap = [(0, warehouse, 0, battery_capacity)] 

    ans = float('inf')
    while heap:
        t, node, mask, bat = heappop(heap)
        if (node, mask, bat) in dp and dp[(node, mask, bat)] <= t:
            continue
        dp[(node, mask, bat)] = t

        if mask == target_mask:
            ans = min(ans, t)
            continue

        for nxt in range(n):
            d = all_dist[node][nxt]
            if d == float('inf') or d > bat:
                continue
            new_mask = mask
            if nxt in customer_index:
                new_mask |= (1 << customer_index[nxt])
            new_bat = bat - d
            if nxt in charging_stations:
                new_bat = battery_capacity
            heappush(heap, (t + d, nxt, new_mask, new_bat))

    return ans if ans < float('inf') else "IMPOSSIBLE"



n = 6
edges = [
    (0,1,2), (1,2,4), (2,3,3),
    (0,4,2), (4,5,2), (5,3,2)
]
warehouse = 0
customers = [2, 3]
charging_stations = [4]
battery_capacity = 5

print(delivery_route_optimizer(n, edges, warehouse, customers, charging_stations, battery_capacity))
