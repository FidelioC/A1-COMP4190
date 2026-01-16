import json
import pytest
import Q1


def load_problem_one_cases():
    with open("test_cases.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["problem_one_cases"]


@pytest.mark.parametrize("case", load_problem_one_cases())
def test_problem_one(case):
    result = Q1.TransformWord(case["beginWord"], case["endWord"], case["wordList"])
    assert result == case["expectedOutput"]
