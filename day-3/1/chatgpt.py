import re


def extract_valid_multiplications(file_path):
    pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
    total_sum = 0

    with open(file_path, "r") as f:
        for line in f:
            matches = pattern.findall(line)
            for x, y in matches:
                total_sum += int(x) * int(y)
    return total_sum


def main():
    input_file = "input.txt"
    result = extract_valid_multiplications(input_file)
    print(f"Sum of valid multiplications: {result}")


if __name__ == "__main__":
    main()
