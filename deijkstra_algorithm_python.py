
def less_cost_node_search():
    min_cost = inf
    min_cost_node = None

    for node in costs.keys():
        if costs[node] < min_cost and node not in processed:
            min_cost = costs[node]
            min_cost_node = node

    return min_cost_node

def  dijstra_function(start_node):
    node = start_node
    while node is not None:
        neibors = graph[node]
        for n in neibors.keys():
            cost = costs[node] + neibors[n]
            if costs[n] > cost:
                costs[n] = cost
                parents[n] = node

        processed.append(node)
        node = less_cost_node_search()


    return costs[finish_node]

def get_final_way():
    result = [finish_node, parents[finish_node]]
    parent = parents[finish_node]

    while parent != None:
        try:
            parent = parents[parent]
            result.append(parent)
        except KeyError:
            parent = None

    result.append(start_node)
    return result[::-1]


inf = float("inf")
processed = []
graph = {"S":{"A": 1,"B": 2,"C": 3}, "A": {"B": 1, "E": 3},
         "C": {"B": 1, "D": 1}, "B": {}, "D": {"E": 4, "F": 2},
         "E": {"F": 2}, "F": {}}
costs = {"S": 0, "A": 1, "B": 2, "C": 3, "D": inf, "E": inf, "F": inf}
parents = {}
start_node = "S"
finish_node = "F"
print(dijkstra_function(start_node))
print(get_final_way())

