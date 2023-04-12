import sys
VERTICES = 6
START = 1
connections = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
connections[0][1] = 1
connections[1][2] = 7
connections[1][4] = 5
connections[4][1] = 1
connections[2][4] = 3
connections[4][3] = 1

def pathfinder(connections, start):
    visited = [False] * VERTICES
    distances = [sys.maxsize] * VERTICES
    distances[start] = 0
    while True:
        minimal_index = sys.maxsize
        minimal_weight = sys.maxsize
        for i in range(VERTICES):
            if not visited[i] and distances[i] < minimal_weight:
                minimal_index = i
                minimal_weight = distances[i]
        if minimal_index == sys.maxsize:
            break
        for i in range(VERTICES):
            if connections[minimal_index][i]:
                temp = minimal_weight + connections[minimal_index][i]
                if temp < distances[i]:
                    distances[i] = temp
        visited[minimal_index] = True
        
    for i in range(VERTICES):
        if distances[i] != sys.maxsize:
            print(f"Вага маршруту: {start} -> {i} = {distances[i]:<6}", end="\t")
            end = i
            weight = distances[end]
            way = f"{end} >- "
            while end != start:
                for j in range(VERTICES):
                    if connections[j][end]:
                        temp = weight - connections[j][end]
                        if temp == distances[j]:
                            end = j
                            weight = temp
                            way += f"{j} >- "
            print("Шлях: ", end="")
            for j in range(len(way)-5, -1, -1):
                print(way[j], end="")
            print()
        else:
            print(f"Вага маршруту: {start} -> {i}  ...  Такого маршруту не існує")
                
pathfinder(connections, START)