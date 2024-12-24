def is_safe_report(levels):
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    if increasing or decreasing:
        for i in range(len(levels) - 1):
            diff = abs(levels[i] - levels[i + 1])
            if diff < 1 or diff > 3:
                return False
        return True
    return False


def count_safe_reports(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_safe_report(levels):
                count += 1
    return count


def count_safe_reports_with_dampener(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            for i in range(len(levels)):
                temp_levels = levels[:i] + levels[i + 1 :]
                if is_safe_report(temp_levels):
                    count += 1
                    break
    return count


filename = "input.txt"
safe_reports = count_safe_reports(filename)
print(f"Number of safe reports: {safe_reports}")

safe_reports_with_dampener = count_safe_reports_with_dampener(filename)
print(f"Number of safe reports with dampener: {safe_reports_with_dampener}")
