import re

with open("food.txt") as f:
    FOOD_DICTIONARY = tuple(map(lambda line: line.strip(), f.read().strip().split("\n")))

with open("illness.txt") as f:
    ILLNESS_DICTIONARY = tuple(map(lambda line: line.strip(), f.read().strip().split("\n")))

def parse(line):
    """Returns dict representing an item parsed from a text line."""

    pattern = re.compile(r"""
    \s*
    (?P<count>\d+)
    \s+
    (?P<description>.*)
    \s+
    at
    \s+
    (?P<pre_taxes_unit_price>\d+\.\d+)
    \s*
    """, re.VERBOSE)

    m = pattern.match(line)
    item = m.groupdict()
    item["count"] = int(item["count"])
    item["pre_taxes_unit_price"] = float(item["pre_taxes_unit_price"])
    item["imported"] = "imported" in item["description"]

    return item

def add_taxes(item):
    """Returns dict identical to item but with taxes informations."""

    item = item.copy() # Don't mutate input dict

    alpha = 1 + 0.10 + 0.05

    if not item.get("imported"):
        alpha -= 0.05

    for token in re.split(r"\s+", item["description"]):
        if token in FOOD_DICTIONARY:
            alpha -= 0.10
            break

        if token in ILLNESS_DICTIONARY:
            alpha -= 0.10
            break

        if token == "book" or token == "books":
            alpha -= 0.10
            break

    item["post_taxes_unit_price"] = item["pre_taxes_unit_price"] * alpha

    return item

def x_to_nearest_y(x, y):
    return y * round(x / y) # https://math.stackexchange.com/a/457889/103884

if __name__ == "__main__":
    from sys import stdin

    lines = []
    while True:
        line = stdin.readline()
        if not line:
            break

        lines.append(line.strip())

    output_lines = []
    total = 0
    sales_taxes = 0

    for line in lines:
        item = add_taxes(parse(line))

        output_lines.append("{} {}: {:.2f}".format(item["count"], item["description"], x_to_nearest_y(item["count"] * item["post_taxes_unit_price"], 0.01)))

        total += item["count"] * item["post_taxes_unit_price"]
        sales_taxes += item["count"] * (item["post_taxes_unit_price"] - item["pre_taxes_unit_price"])

    output_lines.append("Sales taxes: {:.2f}".format(x_to_nearest_y(sales_taxes, 0.05)))
    output_lines.append("Total: {:.2f}".format(x_to_nearest_y(total, 0.01)))

    print("\n".join(output_lines))
