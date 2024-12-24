def evaluate_mul_instructions(memory):
    enabled = True
    result = 0

    for instruction in memory.split("mul"):
        if "(" in instruction and ")" in instruction:
            nums = instruction.split("(")[1].split(")")[0].split("/")
            if len(nums) == 2:
                if enabled:
                    try:
                        num1 = int(nums[0].replace(",", ""))
                        num2 = int(nums[1].replace(",", ""))
                        result += num1 * num2
                    except ValueError:
                        # Handle the conversion error, e.g. provide a default value
                        result += 0
        elif "do()" in instruction:
            enabled = True
        elif "don't()" in instruction:
            enabled = False

    return result


with open("input.txt", "r") as file:
    memory = file.read()

total_result = evaluate_mul_instructions(memory)
print(total_result)
