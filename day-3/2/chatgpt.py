import re


def extract_valid_multiplications(file_path):
    # Corrected regex patterns based on the original instructions
    mul_pattern = re.compile(r"\bmul\((\d{1,3}),(\d{1,3})\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    total_sum = 0
    mul_enabled = True

    with open(file_path, "r") as f:
        for line in f:
            # Find all matches for the patterns
            matches = []
            for pattern in [do_pattern, dont_pattern, mul_pattern]:
                matches.extend([(m.start(), m) for m in pattern.finditer(line)])

            # Sort matches by start position
            matches.sort(key=lambda x: x[0])

            for _, match in matches:
                if match.re == do_pattern:
                    mul_enabled = True
                elif match.re == dont_pattern:
                    mul_enabled = False
                elif match.re == mul_pattern and mul_enabled:
                    x, y = map(int, match.groups())
                    total_sum += x * y

    return total_sum


def main():
    input_file = "input.txt"
    result = extract_valid_multiplications(input_file)
    print(f"Sum of valid multiplications: {result}")


if __name__ == "__main__":
    main()
