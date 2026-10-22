import sys
import heapq
from collections import defaultdict

n = int(input().strip())

trees = []
current_tree = []

for _ in range(n):
    line = input().strip()

    if line.lower() == "break":
        trees.append(current_tree)
        current_tree = []
    else:
        current_tree.append(list(map(int, line.split())))

if current_tree:
    trees.append(current_tree)

start, destination = map(int, input().split())

graph = defaultdict(list)
occurrences = defaultdict(set)

for tree_id, tree in enumerate(trees):
    for row in tree:
        lower = row[0]
        lower_node = (tree_id, lower)

        graph[lower_node]
        occurrences[lower].add(lower_node)

        for upper in row[1:]:
            upper_node = (tree_id, upper)

            graph[upper_node]
            occurrences[upper].add(upper_node)

            graph[lower_node].append((upper_node, 1))
            graph[upper_node].append((lower_node, 0))

for nodes_set in occurrences.values():
    nodes = list(nodes_set)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            graph[nodes[i]].append((nodes[j], 1))
            graph[nodes[j]].append((nodes[i], 1))

if start not in occurrences or destination not in occurrences:
    print(-1)
    sys.exit()

start_node = next(iter(occurrences[start]))
targets = occurrences[destination]

dist = {start_node: 0}
pq = [(0, start_node)]

while pq:
    cost_so_far, node = heapq.heappop(pq)

    if cost_so_far != dist[node]:
        continue

    if node in targets:
        print(cost_so_far)
        sys.exit()

    for neighbor, cost in graph[node]:
        new_cost = cost_so_far + cost

        if new_cost < dist.get(neighbor, float("inf")):
            dist[neighbor] = new_cost
            heapq.heappush(pq, (new_cost, neighbor))

print(-1)