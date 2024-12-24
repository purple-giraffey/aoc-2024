import re


def find_valid_instructions(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    return [(int(x), int(y)) for x, y in matches]


def calculate_total_result(instructions):
    total = 0
    for x, y in instructions:
        total += x * y
    return total


def main():
    with open("input.txt", "r") as file:
        memory = file.read()

    instructions = find_valid_instructions(memory)
    total_result = calculate_total_result(instructions)

    print(f"The total result of the multiplications is: {total_result}")


if __name__ == "__main__":
    main()
