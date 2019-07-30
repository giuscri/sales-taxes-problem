from sales_taxes import x_to_nearest_y
from math import isclose

def test_1dot49_to_nearest_0dot05():
    assert isclose(x_to_nearest_y(1.49, 0.05), 1.50)

def test_1dot2498_to_nearest_0dot01():
    assert isclose(x_to_nearest_y(1.2498, 0.01), 1.25)
