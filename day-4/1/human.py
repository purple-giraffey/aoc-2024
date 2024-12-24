def read():
    with open("input.txt") as raw:
        content = raw.read().split("\n")
        return [list(row) for row in content]


def solve():
    data = read()
    count = 0
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "X":
                if y + 3 < len(row):
                    if (
                        row[y + 1] == "M" and row[y + 2] == "A" and row[y + 3] == "S"
                    ):  # ➡
                        count += 1
                    if x + 3 < len(data):
                        if (
                            data[x + 1][y + 1] == "M"
                            and data[x + 2][y + 2] == "A"
                            and data[x + 3][y + 3] == "S"
                        ):  # ➘
                            count += 1
                if y >= 3:
                    if (
                        row[y - 1] == "M" and row[y - 2] == "A" and row[y - 3] == "S"
                    ):  # ⬅
                        count += 1
                    if x >= 3:
                        if (
                            data[x - 1][y - 1] == "M"
                            and data[x - 2][y - 2] == "A"
                            and data[x - 3][y - 3] == "S"
                        ):  # ↖
                            count += 1
                if x + 3 < len(data):
                    if (
                        data[x + 1][y] == "M"
                        and data[x + 2][y] == "A"
                        and data[x + 3][y] == "S"
                    ):  # ⬇
                        count += 1
                    if y >= 3:
                        if (
                            data[x + 1][y - 1] == "M"
                            and data[x + 2][y - 2] == "A"
                            and data[x + 3][y - 3] == "S"
                        ):  # ↙
                            count += 1
                if x >= 3:
                    if (
                        data[x - 1][y] == "M"
                        and data[x - 2][y] == "A"
                        and data[x - 3][y] == "S"
                    ):  # ⬆
                        count += 1
                    if y + 3 < len(row):
                        if (
                            data[x - 1][y + 1] == "M"
                            and data[x - 2][y + 2] == "A"
                            and data[x - 3][y + 3] == "S"
                        ):  # ↗
                            count += 1

    return count


print(solve())  # 2567
