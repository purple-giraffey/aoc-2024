def count_xmas(word_search):
    count = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            if word_search[i][j] == "X":
                # Check for X-MAS pattern
                if (
                    i + 2 < len(word_search)
                    and j + 2 < len(word_search[i + 2])
                    and j + 2 < len(word_search[i + 2])
                    and word_search[i + 1][j + 1] == "M"
                    and word_search[i + 2][j + 2] == "S"
                ):
                    count += 1
                if (
                    i + 2 < len(word_search)
                    and j - 2 >= 0
                    and j + 2 < len(word_search[i])
                    and word_search[i + 1][j - 1] == "M"
                    and word_search[i + 2][j - 2] == "S"
                ):
                    count += 1
                if (
                    i - 2 >= 0
                    and j + 2 < len(word_search[i])
                    and word_search[i - 1][j + 1] == "M"
                    and word_search[i - 2][j + 2] == "S"
                ):
                    count += 1
                if (
                    i - 2 >= 0
                    and j - 2 >= 0
                    and word_search[i - 1][j - 1] == "M"
                    and word_search[i - 2][j - 2] == "S"
                ):
                    count += 1
    return count


# Read the word search from input.txt
with open("input.txt", "r") as file:
    word_search = [line.strip() for line in file]

# Count the number of X-MAS occurrences
xmas_count = count_xmas(word_search)
print(f"The number of X-MAS occurrences is: {xmas_count}")
