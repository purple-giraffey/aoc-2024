import re


def evaluate_mul_instructions(memory):
    enabled = True
    result = 0
    recent_instruction = ""

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    instructions = re.findall(pattern, memory)

    recent_instruction = ""  # Reset recent_instruction before the loop
    for x, y in instructions:
        if enabled:
            result += int(x) * int(y)

        if "do()" in recent_instruction:
            enabled = True
        elif "don't()" in recent_instruction:
            enabled = False

        if "do()" in memory or "don't()" in memory:
            recent_instruction = memory

    return result


with open("input.txt", "r") as file:
    memory = file.read()

total_result = evaluate_mul_instructions(memory)
print(total_result)
