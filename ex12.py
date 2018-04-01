# ex12
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.


def first_last(numbers):
    return [j for i, j in enumerate(numbers) if i == 0 or i == len(numbers) - 1]


def main():
    a = [5, 10, 15, 20, 25, 10, 15, 20, 25, 10, 15, 20, 25, 10, 15, 20, 22]
    print(first_last(a))


if __name__ == "__main__":
    main()
