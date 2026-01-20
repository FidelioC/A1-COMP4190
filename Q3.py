def ProblemThree():
    print(find_neighbors(2, 0, 3, 3))
    return 0


def hike_dijkstra(heights: list[list[int]]):
    if len(heights) <= 0:
        return 0

    row_length = len(heights)
    col_length = len(heights[0])

    # start from top left
    queue = [(0, 0, 0)]  # row, col, height with prev neighbor
    min_height = 0

    while queue:
        node = queue.pop()
        row, col, height = node
        possible_neighbors = find_neighbors(row, col, row_length, col_length)

    return min_height


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
        list[tuple[int, int]]: list of tuples for the respective neighbors bounded by matrix length (row and column)
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
