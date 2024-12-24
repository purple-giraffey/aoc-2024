def parse_instructions(file_path):
    with open(file_path, "r") as file:
        instructions = file.read()

    mul_instructions = []
    enabled = True
    disabled_mul = False
    mul_sum = 0

    for instruction in instructions.split("mul"):
        if "(" in instruction:
            numbers = instruction.split("(")[1].split(")")[0].split(",")
            if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
                if enabled and not disabled_mul:
                    mul_sum += int(numbers[0]) * int(numbers[1])
                disabled_mul = False
        elif "do()" in instruction:
            enabled = True
        elif "don't()" in instruction:
            enabled = False
            disabled_mul = True

    return mul_sum


file_path = "input.txt"
result = parse_instructions(file_path)
print(result)
