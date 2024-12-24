def read_word_search(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]


def check_mas_variants(m1, a, s1, m2, s2):
    valid_patterns = [
        ("M", "A", "S", "M", "S"),  # Standard MAS
        ("S", "A", "M", "S", "M"),  # Reversed MAS
    ]
    return (m1, a, s1, m2, s2) in valid_patterns


def count_x_mas_pattern(grid):
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if check_mas_variants(
                grid[row - 1][col - 1],
                grid[row][col],
                grid[row + 1][col + 1],
                grid[row - 1][col + 1],
                grid[row + 1][col - 1],
            ):
                pattern_count += 1

            if check_mas_variants(
                grid[row - 1][col + 1],
                grid[row][col],
                grid[row + 1][col - 1],
                grid[row - 1][col - 1],
                grid[row + 1][col + 1],
            ):
                pattern_count += 1

    return pattern_count


def main():
    input_file = "input.txt"
    word_search = read_word_search(input_file)
    occurrences = count_x_mas_pattern(word_search)
    print(f"The X-MAS pattern appears {occurrences} times.")


if __name__ == "__main__":
    main()
