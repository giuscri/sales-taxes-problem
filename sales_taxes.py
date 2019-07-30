def parse(line):
    """Returns dict representing an item parsed from a text line."""

    pass

def add_taxes(item):
    """Returns dict identical to item but with taxes informations."""

    pass

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

        output_lines.append(f'{item["count"]} {item["description"]}: {item["count"] * item["post_taxes_unit_price"]}')

        total += item["count"] * item["post_taxes_unit_price"]
        sales_taxes += item["count"] * (item["post_taxes_unit_price"] - item["pre_taxes_unit_price"])

    output_lines.append("Sales taxes: {:.2f}".format(x_to_nearest_y(sales_taxes, 0.05)))
    output_lines.append("Total: {:.2f}".format(x_to_nearest_y(total, 0.01)))

    print("\n".join(output_lines))
