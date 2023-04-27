import random


def generate_random_decimal(digits=10):
    return [random.randint(0, 9) for _ in range(digits)]


def create_list_of_decimals(n, digits=10):
    decimals = [generate_random_decimal(digits) for _ in range(n)]
    return decimals


def cantors_diagonal_argument(decimals):
    diagonal = [decimals[i][i] for i in range(len(decimals))]
    new_number = [(digit + 1) % 10 for digit in diagonal]
    return new_number


def main():
    n = 10
    decimals = create_list_of_decimals(n)

    print("List of decimals:")
    for decimal in decimals:
        print(f"0.{''.join(map(str, decimal))}")

    new_decimal = cantors_diagonal_argument(decimals)
    print(f"\nNew decimal constructed using Cantor's Diagonal Argument: 0.{''.join(map(str, new_decimal))}")


if __name__ == "__main__":
    main()
