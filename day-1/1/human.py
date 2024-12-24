from typing import List


def read():
    with open("input.txt") as raw:
        content = raw.read()
        list_1: List[int] = []
        list_2: List[int] = []
        for line in content.split("\n"):
            numbers = line.split("   ")
            list_1.append(int(numbers[0]))
            list_2.append(int(numbers[1]))

        list_1.sort()
        list_2.sort()

        return (list_1, list_2)


def solve():
    (list_1, list_2) = read()
    total_dist = 0
    for i in range(len(list_1)):
        total_dist += abs(list_1[i] - list_2[i])
    return total_dist


print(solve())
