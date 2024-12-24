def count_xmas_occurrences():
    with open("input.txt", "r") as file:
        word_search = [line.strip() for line in file]

    word = "XMAS"
    count = 0

    for row in word_search:
        count += row.count(word)

    return count


occurrences = count_xmas_occurrences()
print(f"The word 'XMAS' appears {occurrences} times in the word search.")
