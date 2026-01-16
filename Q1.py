from collections import deque


def ProblemOne():
    begin_word: str = "hit"
    end_word: str = "cog"
    word_list: list[str] = ["hat", "cat", "car", "bar", "bog", "cog"]

    print(TransformWord(begin_word, end_word, word_list))


def TransformWord(begin_word: str, end_word: str, word_list: list[str]):
    # if sk != endWord, return 0
    if word_list[len(word_list) - 1] != end_word:
        return 0

    curr_word: str = begin_word
    total_sequence: int = 0

    queue = deque(word_list)  # initialize double sided queue

    while queue:
        word = queue.popleft()
        if CheckAdjacentWords(curr_word, word):
            curr_word = word
            total_sequence += 1

    # sequence disconnected at the middle somewhere
    if curr_word != end_word:
        return 0

    return total_sequence


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
