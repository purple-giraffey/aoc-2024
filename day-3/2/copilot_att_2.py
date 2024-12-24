import re


def evaluate_mul_instructions(memory):
    enabled = True
    result = 0

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    instructions = re.findall(pattern, memory)

    for x, y in instructions:
        if enabled:
            result += int(x) * int(y)

        if "do()" in memory:
            enabled = True
        elif "don't()" in memory:
            enabled = False

    return result


with open("input.txt", "r") as file:
    memory = file.read()

total_result = evaluate_mul_instructions(memory)
print(total_result)
