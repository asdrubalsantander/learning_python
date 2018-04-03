#! /usr/bin/env python
# 13-fibonacci
# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.


def generate_fibonacci(number, fibonacci):
    fibonacci.append(fibonacci[number - 1] + fibonacci[number - 2])
    return fibonacci


def main():
    number = int(input("How many numbers in the fibonacci sequence: "))

    if number == 0:
        fibonacci = [0]
    else:
        fibonacci = [0, 1]

        for i in range(2, number + 1):
            generate_fibonacci(i, fibonacci)

    print(fibonacci)


if __name__ == "__main__":
    main()
