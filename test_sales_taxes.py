from sales_taxes import x_to_nearest_y, parse, add_taxes, x_to_next_y
from math import isclose
import pytest, subprocess

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
    expected = {"count": 3, "description": "imported box of chocolates", "pre_taxes_unit_price": 11.25, "imported": True}
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

def test_e2e_with_input1():
    with open("input1") as f:
        input1 = f.read()

    process = subprocess.run(["python3", "sales_taxes.py"], stdout=subprocess.PIPE, input=input1, encoding="utf-8")
    assert process.stdout == "2 book: 24.98\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.50\nTotal: 42.32\n"

def test_e2e_with_input2():
    with open("input2") as f:
        input2 = f.read()

    process = subprocess.run(["python3", "sales_taxes.py"], stdout=subprocess.PIPE, input=input2, encoding="utf-8")
    assert process.stdout == "1 imported box of chocolates: 10.50\n1 imported bottle of perfume: 54.65\nSales Taxes: 7.65\nTotal: 65.15\n"

def test_e2e_with_input3():
    with open("input3") as f:
        input3 = f.read()

    process = subprocess.run(["python3", "sales_taxes.py"], stdout=subprocess.PIPE, input=input3, encoding="utf-8")
    assert process.stdout == "1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89\n1 packet of headache pills: 9.75\n3 imported box of chocolates: 35.55\nSales Taxes: 7.90\nTotal: 98.38\n"

def test_e2e_with_0xb2_book():
    process = subprocess.run(["python3", "sales_taxes.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=b"\xb2 book at 12.49")
    assert process.stderr.startswith(b"[fatal]")
    assert process.returncode == 1

def test_e2e_with_r_book():
    process = subprocess.run(["python3", "sales_taxes.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, input="r book at 12.49", encoding="utf-8")
    assert process.stderr.startswith("[fatal]")
    assert process.returncode == 1

def test_e2e_with_empty_input():
    process = subprocess.run(["python3", "sales_taxes.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, input="", encoding="utf-8")
    assert process.stderr.startswith("[fatal]")
    assert process.returncode == 1

if __name__ == "__main__":
    pytest.main()
