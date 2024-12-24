def read():
    with open("input.txt") as raw:
        content = raw.read().split("\n")
        return [list(row) for row in content]


def solve():
    data = read()
    count = 0
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if (
                char == "A"
                and y - 1 >= 0
                and y + 1 < len(row)
                and x - 1 >= 0
                and x + 1 < len(data)
            ):
                if data[x - 1][y - 1] == "M" and data[x + 1][y + 1] == "S":
                    if (data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S") or (
                        data[x - 1][y + 1] == "S" and data[x + 1][y - 1] == "M"
                    ):
                        count += 1
                elif data[x - 1][y - 1] == "S" and data[x + 1][y + 1] == "M":
                    if (data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S") or (
                        data[x - 1][y + 1] == "S" and data[x + 1][y - 1] == "M"
                    ):
                        count += 1

    return count


print(solve())  # 2029
