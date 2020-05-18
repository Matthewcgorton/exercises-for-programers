#!/usr/local/bin/python3
import sys


def get_number(prompt):

    while True:
        number_str = input(prompt)

        try:
            number = float(number_str)

        except ValueError as e:
            print(f"'{number_str}' is not a number")
            continue

        if "." in number_str:
            number = float(number_str)
        else:
            number = int(number_str)

        if number < 0:
            print("Number must be positive")
            continue

        return number


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


def main(argv):

    number_1 = get_number("What is the first number? ")
    number_2 = get_number("What is the second number? ")

    print(f"\nNumber 1: {number_1}, Number 2: {number_2}\n\n")

    print(f"{number_1} + {number_2} = {add(number_1, number_2)}\n" +
          f"{number_1} - {number_2} = {subtract(number_1, number_2)}\n" +
          f"{number_1} * {number_2} = {multiply(number_1, number_2)}\n" +
          f"{number_1} / {number_2} = {divide(number_1, number_2)}\n"
          )



if __name__ == '__main__':
    main(sys.argv)
