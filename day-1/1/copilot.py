def calculate_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0

    for left_num, right_num in zip(left_list, right_list):
        distance = abs(left_num - right_num)
        total_distance += distance

    return total_distance


# Read input from input.txt
with open("input.txt", "r") as file:
    lines = file.readlines()

left_list = []
right_list = []

# Parse the input and populate the left and right lists
for line in lines:
    left_num, right_num = map(int, line.strip().split())
    left_list.append(left_num)
    right_list.append(right_num)

# Calculate the total distance between the lists
distance = calculate_distance(left_list, right_list)
print(f"The total distance between the lists is: {distance}")
