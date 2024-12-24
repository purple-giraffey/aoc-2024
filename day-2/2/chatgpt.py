def is_safe_report(levels):
    increasing = all(0 < levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(
        -3 <= levels[i + 1] - levels[i] < 0 for i in range(len(levels) - 1)
    )
    return increasing or decreasing


def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True
    for i in range(len(levels)):
        reduced_levels = levels[:i] + levels[i + 1 :]
        if is_safe_report(reduced_levels):
            return True
    return False


def count_safe_reports(file_path):
    safe_count = 0
    with open(file_path, "r") as f:
        for line in f:
            levels = list(map(int, line.split()))
            if is_safe_with_dampener(levels):
                safe_count += 1
    return safe_count


def main():
    input_file = "input.txt"
    safe_reports = count_safe_reports(input_file)
    print(f"Number of safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
