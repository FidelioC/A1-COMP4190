import math


def ProblemThree():
    heights = [[1, 10, 6], [1, 1, 1], [1, 1, 1]]
    print(find_neighbors(2, 0, 3, 3))
    print(hike_dijkstra(heights))
    return 0


def hike_dijkstra(heights: list[list[int]]):
    if not heights or not heights[0]:
        return 0

    row_length = len(heights)
    col_length = len(heights[0])

    # start from top left
    queue = [(0, 0, 0)]  # row, col, height with prev neighbor

    # to record each node height effort so far
    distance = [[math.inf for _ in range(col_length)] for _ in range(row_length)]
    distance[0][0] = 0

    while queue:
        queue.sort(key=lambda x: x[2])  # sort the queue by height ascending
        row, col, height = queue.pop(0)  # get the lowest possible height step

        # reached the end
        if row == row_length - 1 and col == col_length - 1:
            return height

        # get the node height we are currently at
        curr_node_height = heights[row][col]

        # for the current node, calculate all possible neighbors height step
        possible_neighbors = find_neighbors(row, col, row_length, col_length)
        for neighbor_row, neighbor_col in possible_neighbors:
            neighbor_height = heights[neighbor_row][neighbor_col]

            # step between neighbor and the current node
            height_step = abs(curr_node_height - neighbor_height)

            # get the maximum absolute difference
            new_distance = max(height, height_step)

            # only append to queue if new max absolute difference is
            # lower than the last recorded distance
            if new_distance < distance[neighbor_row][neighbor_col]:
                distance[neighbor_row][neighbor_col] = new_distance
                # calculate the height step between each of the neighbor with the current node
                queue.append(
                    (
                        neighbor_row,
                        neighbor_col,
                        new_distance,
                    )
                )

    return 0


def find_neighbors(
    row: int, col: int, row_length: int, col_length: int
) -> list[tuple[int, int]]:
    """Given row and col, calculate the respective neighbors (bounded by the row and col length)

    Args:
        row (int): index row
        col (int): index column
        row_length (int): length of matrix row
        col_length (int): length of matrix column

    Returns:
        list[tuple[int, int]]: list of tuples for the respective neighbors index bounded by matrix length (row and column)
    """
    left = (0, -1)
    right = (0, 1)
    top = (-1, 0)
    bottom = (1, 0)

    neighbors_calc = [left, right, top, bottom]

    curr_height = (row, col)
    neighbors_indices = []

    for calc in neighbors_calc:
        # calculate respective neighbors
        curr_neighbor = tuple(x + y for x, y in zip(curr_height, calc))

        # bounds check
        neighbor_x, neighbor_y = curr_neighbor
        if 0 <= neighbor_x < row_length and 0 <= neighbor_y < col_length:
            neighbors_indices.append(curr_neighbor)

    return neighbors_indices


def main():
    ProblemThree()


if __name__ == "__main__":
    main()
