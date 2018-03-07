import pytest
from csvfile import returnData

#passed tests will return True 

def test_bool():
    assert True

def test_empty_index():
    data = returnData()
    for i in data:
        for l in range(0, len(i)):
            assert i[l] != ""
