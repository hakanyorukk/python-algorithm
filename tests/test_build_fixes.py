import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from a2 import exercise_1, exercise_2
from basic_math_recursion.task3 import exercise_4


def test_status_code_breakdown_exercise_1():
    records = [{"status_code": "200"}, {"status_code": "404"}, {"status_code": "500"}]
    assert exercise_1.status_code_breakdown(records) == {"2xx": 1, "4xx": 1, "5xx": 1}


def test_status_code_breakdown_exercise_2():
    records = [{"status": "200"}, {"status": "403"}, {"status": "200"}]
    assert exercise_2.status_code_breakdown(records) == {"2xx": 2, "4xx": 1}


def test_fibonaacci_function_available_and_works():
    assert exercise_4.fibonaacci(5) == 5
