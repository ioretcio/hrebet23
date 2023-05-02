import sys

connections = [
    [0, 2, 4, 2, 0, 0],
    [0, 0, 0, 6, 0, 10],
    [0, 4, 0, 0, 0, 1],
    [0, 4, 9, 0, 6, 0],
    [0, 0, 5, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]


def pathfinder(pfinderConnections, start):
    VERTICES = len(pfinderConnections)
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
            if pfinderConnections[minimal_index][i]:
                temp = minimal_weight + pfinderConnections[minimal_index][i]
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
                    if pfinderConnections[j][end]:
                        temp = weight - pfinderConnections[j][end]
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


if __name__ == "__main__":
    pathfinder(connections, 0)