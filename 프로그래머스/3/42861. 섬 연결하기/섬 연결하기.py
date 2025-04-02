def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    # 유니온 파인드
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):
            total_cost += cost

    return total_cost