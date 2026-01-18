import json
import pytest
import Q1
import Q2
from enum import StrEnum


class CasesMetaData(StrEnum):
    """Enumerables

    Args:
        StrEnum (_type_): string enumerables for the test cases json
    """

    CASES_TEST_ONE = "problem_one_cases"
    CASES_TEST_TWO = "problem_two_cases"


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
