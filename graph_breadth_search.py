"""algorith breadth search in graph. If there is node equal finish point in grap"""

from collections import deque

def if_finish_point(point):
    return point == finish_point

def search(start_point):
    # name is start point of searching
    search_queue = deque()
    search_queue += graph[start_point]
    searched = []

    while search_queue:
        point = search_queue.popleft()
        if point not in searched:
            if if_finish_point(point):
                return True
            else:
                try:
                    search_queue += graph[point]
                    searched.append(point)
                except KeyError:
                    continue

    return False

graph = {"A": ["B", "C", "D"], "B": ["E"], "C": ["E", "D", "H"], "D": ["H"], "E": ["H"]}
start_point = "A"
finish_point = "B"
print(search(start_point))
