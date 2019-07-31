from sales_taxes import x_to_nearest_y, parse, add_taxes, x_to_next_y
from math import isclose
import pytest

def test_1dot49_to_nearest_0dot05():
    assert isclose(x_to_nearest_y(1.49, 0.05), 1.50)

def test_1dot2498_to_nearest_0dot01():
    assert isclose(x_to_nearest_y(1.2498, 0.01), 1.25)

def test_54dot62499_to_next_0dot05():
    assert isclose(x_to_next_y(54.62499, 0.05), 54.65)

def test_0dot5625_to_next_0dot05():
    assert isclose(x_to_next_y(0.5625, 0.05), 0.6)

def test_parse_2_books_at_12dot49():
    actual = parse("2 books at 12.49")
    expected = {"count": 2, "description": "books", "pre_taxes_unit_price": 12.49, "imported": False}
    assert actual["count"] == expected["count"]
    assert actual["description"] == expected["description"]
    assert isclose(actual["pre_taxes_unit_price"], expected["pre_taxes_unit_price"])
    assert actual["imported"] == expected["imported"]

def test_parse_1_imported_bottle_of_perfume_at_27dot99():
    actual = parse("1 imported bottle of perfume at 27.99")
    expected = {"count": 1, "description": "imported bottle of perfume", "pre_taxes_unit_price": 27.99, "imported": True}
    assert actual["count"] == expected["count"]
    assert actual["description"] == expected["description"]
    assert isclose(actual["pre_taxes_unit_price"], expected["pre_taxes_unit_price"])
    assert actual["imported"] == expected["imported"]

def test_parse_3_box_of_chocolates_at_11dot25():
    actual = parse("3 box of imported chocolates at 11.25")
    expected = {"count": 3, "description": "box of imported chocolates", "pre_taxes_unit_price": 11.25, "imported": True}
    assert actual["count"] == expected["count"]
    assert actual["description"] == expected["description"]
    assert isclose(actual["pre_taxes_unit_price"], expected["pre_taxes_unit_price"])
    assert actual["imported"] == expected["imported"]

def test_add_taxes_on_2_books():
    item = add_taxes({"description": "books", "pre_taxes_unit_price": 12.49})
    assert isclose(item["post_taxes_unit_price"], 12.49)

def test_add_taxes_on_1_chocolate_bar():
    item = add_taxes({"description": "chocolate bar", "pre_taxes_unit_price": 0.85})
    assert isclose(item["post_taxes_unit_price"], 0.85)

def test_add_taxes_on_1_packet_of_headache_pills():
    item = add_taxes({"description": "packet of headache pills", "pre_taxes_unit_price": 9.75})
    assert isclose(item["post_taxes_unit_price"], 9.75)

def test_add_taxes_on_1_imported_box_of_chocolates():
    item = add_taxes({"description": "imported box of chocolates", "pre_taxes_unit_price": 10.00, "imported": True})
    assert isclose(item["post_taxes_unit_price"], 10.50)

def test_add_taxes_on_1_music_cd():
    item = add_taxes({"description": "music CD", "pre_taxes_unit_price": 14.99})
    assert isclose(item["post_taxes_unit_price"], 16.49)

def test_add_taxes_on_imported_bottle_of_perfume():
    item = add_taxes({"description": "imported bottle of perfume", "pre_taxes_unit_price": 27.99, "imported": True})
    assert isclose(item["post_taxes_unit_price"], 32.19)

if __name__ == "__main__":
    pytest.main()
