def is_safe_report(levels):
    if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) or all(
        levels[i] > levels[i + 1] for i in range(len(levels) - 1)
    ):
        if all(
            1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)
        ):
            return True
    return False


def count_safe_reports(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_safe_report(levels):
                count += 1
    return count


file_path = "input.txt"  # Replace with the actual file path
safe_reports = count_safe_reports(file_path)
print(f"The number of safe reports is: {safe_reports}")
