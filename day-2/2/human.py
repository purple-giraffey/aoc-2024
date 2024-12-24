from typing import List


def read():
    with open("input.txt") as raw:
        content = raw.read()
        data: List[list[int]] = []
        for line in content.split("\n"):
            numbers = line.split(" ")
            data.append([int(i) for i in numbers])
        return data


def is_safe(array: List[int]) -> bool:
    is_increasing = None
    for i in range(1, len(array)):
        diff = abs(array[i] - array[i - 1])
        if diff < 1 or diff > 3:
            return False
        if is_increasing is None:
            is_increasing = array[i] > array[i - 1]
        else:
            if (
                array[i] > array[i - 1]
                and not is_increasing
                or array[i] < array[i - 1]
                and is_increasing
            ):
                return False
    return True


def safe_with_retry(row):
    for i in range(len(row)):
        row_copy = list(row)
        row_copy.pop(i)
        if is_safe(row_copy):
            return True
    return False


def solve():
    data = read()
    count = 0
    for row in data:
        if is_safe(row) or safe_with_retry(row):
            count += 1
    return count


print(solve())  # 324
