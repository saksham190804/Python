import heapq
def uniform_cost_search(graph, start, goal):
    front = [(0, start)]  # (cost, node)
    explored = set()

    while front:
        cost, current_node = heapq.heappop(front)
        if current_node == goal:
            return cost
        explored.add(current_node)
        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in explored:
                total_cost = cost + neighbor_cost
                heapq.heappush(front, (total_cost, neighbor))
    return None
graph = {
    'S': {'A': 1, 'B': 5, 'C': 15},'A': {'G': 10},'B': {'G': 5},'C': {'G': 5},'G': {}
}
start_node = 'S'
goal_node = 'G'

result = uniform_cost_search(graph, start_node, goal_node)
if result is not None:
    print(f"Cost from {start_node} to {goal_node} : {result}")
else:
    print(f"No path found from {start_node} to {goal_node}")
