import MYDB   #pytest parameters
import pytest

@pytest.mark.parametrize("test_input,expected_output",[(2,4),(3,9),(4,16)])
def test_multiplication(test_input,expected_output):
    result=MYDB.multiplication(test_input)
    assert result==expected_output
