from collections import deque


def TransformWord(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """Transform word sequence, breadth first search

    Args:
        begin_word (str): begin word
        end_word (str): end word
        word_list (list[str]): list of words

    Returns:
        _type_: total number of sequence steps
    """
    # if end word not in list
    if end_word not in word_list:
        return 0

    queue = deque()  # initialize double sided queue
    visited = set()
    start_sequence = 1
    queue.append((begin_word, start_sequence))

    while queue:
        queue_word, sequence = queue.popleft()
        for list_word in word_list:
            if list_word not in visited and CheckAdjacentWords(queue_word, list_word):
                if list_word == end_word:
                    return sequence + 1
                queue.append((list_word, sequence + 1))
                visited.add(list_word)

    return 0


def CheckAdjacentWords(str_one: str, str_two: str) -> bool:
    """
    Compare two strings,
    check whether the adjacent strings differs by a single letter

    Args:
        str_one (str): string one
        str_two (str): string two

    Returns:
        bool: True -> difference is one char
    """
    if len(str_one) != len(str_two):
        return False

    difference: int = 0
    for i in range(len(str_one)):
        if str_one[i] != str_two[i]:
            difference += 1
            if difference >= 2:
                return False

    return difference == 1


def main():
    begin_word: str = "hit"
    end_word: str = "cog"
    word_list: list[str] = ["hot", "dot", "dog", "lot", "log", "cog"]

    print("Question 1 Output: ")
    print(TransformWord(begin_word, end_word, word_list))


if __name__ == "__main__":
    main()
