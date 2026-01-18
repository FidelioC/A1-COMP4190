def ProblemTwo():
    isConnected: list[list[int]] = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    count = CountProvinces(isConnected)
    print(count)


def CountProvinces(is_connected: list[list[int]]) -> int:
    visited = set()
    count: int = 0

    for i in range(len(is_connected)):
        if i not in visited:
            visited.add(i)
            DFS(is_connected, visited, i)
            count += 1

    return count


def DFS(is_connected: list[list[int]], visited: set, city_index: int):
    for connection in range(len(is_connected)):
        if connection not in visited and is_connected[city_index][connection] == 1:
            visited.add(connection)
            DFS(is_connected, visited, connection)
