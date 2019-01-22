"""breadth search algorithm of findind shortest way(in steps) in graph
    returns the way
"""
from collections import deque

def if_final_point(point):

    return point == final_point


def get_final_way(parents):

    parent = parents[final_point]
    result = str(final_point)

    while(parent != None):
        result += str(parent)
        parent = parents[parent]

    return result[::-1]


def search(start_point):

    parents = {}
    parents[start_point] = None
    searched = []
    searched.append(start_point)
    search_queue = deque()
    search_queue.append(start_point)

    while search_queue:
        parent =  search_queue.popleft()
        try:
            points = graph[parent]
        except KeyError:
            points = []

        for point in points:
            parents[point] = parent
            if point not in searched:
                if if_final_point(point):
                    return get_final_way(parents)
                else:
                    search_queue.append(point)
                    searched.append(point)
    return None

graph = {1: [2, 3, 4], 2: [5], 3: [5, 6, 4], 4: [6], 5: [6]}
start_point = 1
final_point = 6
print(search(start_point))
