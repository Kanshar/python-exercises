import pytest
from profit import get_max_profit

def test_simple(capsys):
    testData = [
        { 'input': [], 'output': 0 },
        { 'input': [5], 'output': 0 },
        { 'input': [5,6], 'output': 1 },
        { 'input': [10, 7, 5, 8, 11, 9], 'output': 6 },
        { 'input': [5, 10, 7, 8, 11, 9], 'output': 6 },
        { 'input': [11, 5, 10, 7, 8, 9], 'output': 5 },
        { 'input': [9, 11, 5, 10, 3, 4, 6, 6, 6], 'output': 5 },
        { 'input': [9, 11, 5, 4, 5, 10, 7, 8, 9, 4], 'output': 6 },
        { 'input': [3, 9, 11, 5, 4, 5, 10, 7, 8, 9, 14], 'output': 11 },
        { 'input': [10, 9, 11, 5, 4, 5, 3, 7, 8, 9, 14], 'output': 11 },
        { 'input': [6, 14, 5, 6, 5, 10, 7, 8, 9, 10, 11], 'output': 8 },
        { 'input': [7, 12, 9, 6, 11, 10, 8, 9, 7, 8, 9, 8], 'output': 5 },
        { 'input': [1.3, 2.4, 3.6, 4.7, 5.38, 6.94, 7.21, 8.62, 9.94, 10.93, 11.02, 12.07], 'output': 10.77 },
        { 'input': [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'output': 0 }
    ]
    for data in testData:
        print(data)
        res = get_max_profit(data["input"])
        assert res == data["output"]

def test_oneday():
    testData = [
        { 'input': [10, 7, 5, 8, 11, 9]*10*24, 'output': 6 },
        { 'input': [5, 10, 7, 8, 11, 9]*10*24, 'output': 6 },
        { 'input': [11, 5, 10, 7, 8, 9]*10*24, 'output': 6 },
        { 'input': [9, 11, 5, 10, 3, 4, 6, 6, 6]*10*16, 'output': 8 },
        { 'input': [9, 11, 5, 4, 5, 10, 7, 8, 9, 4]*6*24, 'output': 7 },
        { 'input': [3, 9, 11, 5, 4, 5, 10, 7, 8, 9, 14, 2]*10*12, 'output': 12 },
        { 'input': [10, 9, 11, 15, 4, 5, 3, 7, 8, 9, 14, 6]*10*12, 'output': 12 },
        { 'input': [6, 14, 5, 6, 5, 10, 7, 8, 9, 10, 11, 9]*10*12, 'output': 9 },
        { 'input': [7, 12, 9, 6, 11, 10, 8, 9, 7, 8, 9, 8]*10*12, 'output': 6 },
        { 'input': [1.3, 2.4, 3.6, 4.7, 5.38, 6.94, 7.21, 8.62, 9.94, 10.93, 11.02, 12.07]*10*12, 'output': 10.77 },
        { 'input': [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]*10*12, 'output': 11 }
    ]
    for data in testData:
        res = get_max_profit(data["input"])
        assert res == data["output"]

def test_errdata():
        res = get_max_profit(['as', 'a', 'str', 'go', 'forth'])
        assert res == -1

