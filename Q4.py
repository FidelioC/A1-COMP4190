def FindGoal(graph: dict[int, list[int]], start: int, goal: int, max_depth: int) -> int:
    curr_max_depth = 0
    while True:
        depth_result = DepthGoalSearch(graph, 0, start, goal, curr_max_depth)
        if depth_result != -1:
            return depth_result
        if curr_max_depth >= max_depth:
            return -1
        curr_max_depth += 1


def DepthGoalSearch(
    graph: dict[int, list[int]], depth: int, node: int, goal: int, curr_max_depth: int
):
    if node == goal:
        return depth

    if depth == curr_max_depth:
        return -1

    children = graph[node]

    if not children:
        return -1

    for child in children:
        result = DepthGoalSearch(graph, depth + 1, child, goal, curr_max_depth)

    return result


def main():
    graph = {
        0: [1, 2],
        1: [3],
        2: [4, 5],
        3: [],
        4: [],
        5: [6],
        6: [],
    }
    start = 0
    goal = 6
    max_depth = 5

    print("Question 4 Output: ")
    print(FindGoal(graph, start, goal, max_depth))


if __name__ == "__main__":
    main()
