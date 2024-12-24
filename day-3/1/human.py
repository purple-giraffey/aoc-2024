import re


def read():
    with open("input.txt") as raw:
        content = raw.read()
        return content


def get_instruction_data(data):
    return re.finditer(r"(mul)\([0-9]{1,3},[0-9]{1,3}\)", data)


def solve():
    data = read()
    instruction_data = get_instruction_data(data)
    sum = 0
    for r in instruction_data:
        match = r.group()
        numbers = match[4 : len(match) - 1].split(",")
        sum += int(numbers[0]) * int(numbers[1])
    return sum


print(solve())  # 166630675
