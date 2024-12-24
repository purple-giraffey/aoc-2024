left_list = []
right_list = []

# Read the left and right lists from the input.txt file
with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Create a dictionary to store the count of each number in the right list
right_count = {}
for number in right_list:
    right_count[number] = right_count.get(number, 0) + 1

# Initialize the similarity score to 0
similarity_score = 0

# Iterate over each number in the left list
for number in left_list:
    # Check if the number exists in the dictionary
    if number in right_count:
        # Multiply the number by its count in the right list and add it to the similarity score
        similarity_score += number * right_count[number]

# Print the similarity score
print(similarity_score)
