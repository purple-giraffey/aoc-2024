def evaluate_mul_instructions(memory):
    enabled = True
    result = 0

    i = 0
    while 0 <= i < len(memory):
        if memory[i : i + 4] == "mul(":
            if enabled:
                j = i + 4
                while memory[j] != ",":
                    j += 1
                x = int("".join(filter(str.isdigit, memory[i + 4 : j])))

                k = j + 1
                while memory[k] != ")":
                    k += 1
                y_str = "".join(filter(str.isdigit, memory[j + 1 : k]))
                y = int(y_str) if y_str else 0

                result += x * y

            i = k + 1 if enabled else i + 1
        elif memory[i] == "d" and memory[i + 1] == "o" and memory[i + 2] == "(":
            enabled = True
            i += 3
        elif (
            memory[i] == "d"
            and memory[i + 1] == "o"
            and memory[i + 2] == "n"
            and memory[i + 3] == "'"
            and memory[i + 4] == "t"
            and memory[i + 5] == "("
        ):
            enabled = False
            i += 5
        else:
            i += 1

    return result


with open("input.txt", "r") as file:
    memory = file.read().strip()

result = evaluate_mul_instructions(memory)
print(result)
