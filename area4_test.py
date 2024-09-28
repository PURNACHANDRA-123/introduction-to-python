import area3
import pytest
import sys
@pytest.mark.skipif(sys.version_info < (3, 10), reason="no way of currently testing this")
def test_calc_total():
    total=area3.calc_total(3,4)
    assert total==7


def test_calc_mul():
    total=area3.calc_mul(3,4)
    assert total==12


def test_dummy():
    assert True

@pytest.mark.windows
def test_window():
    assert True
@pytest.mark.windows
def test_window2():
    assert True


@pytest.mark.mac
def test_mac():
    assert True








