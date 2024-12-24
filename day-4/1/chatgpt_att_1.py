def read_word_search(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]


def count_word_in_direction(grid, word, row, col, d_row, d_col):
    count = 0
    word_len = len(word)
    rows, cols = len(grid), len(grid[0])

    while 0 <= row < rows and 0 <= col < cols:
        if all(
            0 <= row + i * d_row < rows
            and 0 <= col + i * d_col < cols
            and grid[row + i * d_row][col + i * d_col] == word[i]
            for i in range(word_len)
        ):
            count += 1
        row += d_row
        col += d_col

    return count


def count_word_occurrences(grid, word):
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # up-left
        (-1, 1),  # up-right
    ]

    total_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for d_row, d_col in directions:
                total_count += count_word_in_direction(
                    grid, word, row, col, d_row, d_col
                )

    return total_count


def main():
    input_file = "input.txt"
    word_search = read_word_search(input_file)
    target_word = "XMAS"
    occurrences = count_word_occurrences(word_search, target_word)
    print(f'The word "{target_word}" appears {occurrences} times.')


if __name__ == "__main__":
    main()
