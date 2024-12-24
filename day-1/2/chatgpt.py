from collections import Counter


def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, "r") as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    similarity_score = sum(left * right_count[left] for left in left_list)
    return similarity_score


def main():
    input_file = "input.txt"
    left_list, right_list = read_input(input_file)
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity score: {similarity_score}")


if __name__ == "__main__":
    main()
