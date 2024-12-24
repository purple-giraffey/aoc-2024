def evaluate_mul_instructions(memory):
    enabled = True
    result = 0

    i = 0
    while i < len(memory):
        if memory[i : i + 4] == "mul(":
            if enabled:
                j = i + 4
                while memory[j] != ",":
                    j += 1
                x = int(memory[i + 4 : j])

                j += 1
                k = j
                while memory[k] != ")":
                    k += 1
                y = int(memory[j:k])

                result += x * y

            i = k + 1
        elif memory[i : i + 4] == "do()":
            enabled = True
            i += 4
        elif memory[i : i + 6] == "don't()":
            enabled = False
            i += 6
        else:
            i += 1

    return result


# Read the corrupted memory from input.txt
with open("input.txt", "r") as file:
    memory = file.read()

# Evaluate the mul instructions
total_result = evaluate_mul_instructions(memory)

print(total_result)
