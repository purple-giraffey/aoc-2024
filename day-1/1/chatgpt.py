def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, "r") as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance


def main():
    input_file = "input.txt"
    left_list, right_list = read_input(input_file)
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {total_distance}")


if __name__ == "__main__":
    main()
