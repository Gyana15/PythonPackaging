import csv
from pytest import fixture, mark

data_path = "C:/Users/GYAN/PycharmProjects/pythonProject2/Test_Data/FL_insurance_sample.csv"

def getVal() :
    ifile = open(data_path, "r")
    read = csv.reader(ifile)
    fields = next(read)
    for field in fields:
        if(field == 'Execute'):
            colCount = fields
            print(colCount)
    arrays = []
    for row in read :
        if(row[0]=='Y'):
            arrays.append(row[2])
    print(arrays)
    return arrays

@fixture(params=getVal())
def test_fixture(request):
    test_data=request.param
    return test_data

@mark.smoke
def test_get_value(test_fixture) :
    print("The values are : ")
    print(test_fixture, "dermant")