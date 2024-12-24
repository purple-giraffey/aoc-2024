import re


def read():
    with open("input.txt") as raw:
        content = raw.read()
        return content


def get_instruction_data(data):
    return re.finditer(r"(mul)\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data)


def solve():
    data = read()
    instruction_data = get_instruction_data(data)
    sum = 0
    apply = True
    for r in instruction_data:
        match = r.group()
        print(match)
        if match.startswith("mul") and apply:
            numbers = match[4 : len(match) - 1].split(",")
            sum += int(numbers[0]) * int(numbers[1])
        if match == "don't()":
            apply = False
        if match == "do()":
            apply = True
    return sum


print(solve())  # 93465710
