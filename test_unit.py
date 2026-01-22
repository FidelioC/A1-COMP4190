import json
import pytest
import Q1
import Q2
import Q3
import Q4
from enum import StrEnum


class CasesMetaData(StrEnum):
    """Enumerables

    Args:
        StrEnum (_type_): string enumerables for the test cases json
    """

    CASES_TEST_ONE = "problem_one_cases"
    CASES_TEST_TWO = "problem_two_cases"
    CASES_TEST_THREE = "problem_three_cases"
    CASES_TEST_FOUR = "problem_four_cases"


def load_problem_test_cases(test_cases_name: str):
    """load the test cases from a json file

    Args:
        test_cases_name (str): the test cases problem identifier

    Returns:
        _type_: a list of test cases for that specific problem
    """
    with open("test_cases.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[test_cases_name]


@pytest.mark.parametrize(
    "case", load_problem_test_cases(CasesMetaData.CASES_TEST_ONE.value)
)
def test_problem_one(case):
    result = Q1.TransformWord(case["beginWord"], case["endWord"], case["wordList"])
    assert result == case["expectedOutput"]


# ==== PROBLEM TWO TESTS ==== #
@pytest.mark.parametrize(
    "case", load_problem_test_cases(CasesMetaData.CASES_TEST_TWO.value)
)
def test_problem_two(case):
    result = Q2.CountProvinces(case["isConnected"])
    assert result == case["expectedOutput"]


# ==== PROBLEM THREE TESTS ==== #
@pytest.mark.parametrize(
    "case", load_problem_test_cases(CasesMetaData.CASES_TEST_THREE.value)
)
def test_problem_three(case):
    result = Q3.HikeDijkstra(case["heights"])
    assert result == case["expectedOutput"]


# ==== PROBLEM FOUR TESTS ==== #
@pytest.mark.parametrize(
    "case", load_problem_test_cases(CasesMetaData.CASES_TEST_FOUR.value)
)
def test_problem_four(case):
    graph = {int(k): v for k, v in case["graph"].items()}
    result = Q4.FindGoal(graph, case["start"], case["goal"], case["max_depth"])
    assert result == case["expectedOutput"]
