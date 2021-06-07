import csv
import pytest_expect
import pytest
from pytest import mark

data_path = "C:/Users/GYAN/PycharmProjects/pythonProject2/Test_Data/FL_insurance_sample.csv"


def getVal():
    ifile = open(data_path, "r")
    read = csv.reader(ifile)
    fields = next(read)
    arrays = []
    for row in read:
        if row[0] == 'Y':
            arrays.append(row[2])
    print(arrays)
    return arrays


@mark.smoke
@mark.parametrize("value", getVal())
def test_get_value(value):
    print("The values are : ")
    print(value, "dermant")
    assert 0 == 1, "Values not equal"


@pytest.fixture
def test_fixture():
    print("fixture")
