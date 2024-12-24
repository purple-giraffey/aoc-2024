def read_word_search(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]


def count_x_mas_pattern(grid):
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Check first X-MAS pattern
            if (
                grid[row - 1][col - 1] == "M"
                and grid[row][col] == "A"
                and grid[row + 1][col + 1] == "S"
                and grid[row - 1][col + 1] == "M"
                and grid[row + 1][col - 1] == "S"
            ):
                pattern_count += 1

            # Check second X-MAS pattern (mirrored diagonally)
            if (
                grid[row - 1][col + 1] == "M"
                and grid[row][col] == "A"
                and grid[row + 1][col - 1] == "S"
                and grid[row - 1][col - 1] == "M"
                and grid[row + 1][col + 1] == "S"
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
