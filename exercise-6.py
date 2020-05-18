#!/usr/local/bin/python3
import sys
from datetime import date



def get_number(prompt, max=None):

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

        if max is not None and number > max:
            print(f"Number is greater that max allow value: {max}")
            continue

        return number


def main(argv):

    age = get_number("What is you age? ")
    retirement_age = get_number("What age do you to be when you retire? ", max=100)

    print(f"\nAge: {age}, Retirement Age: {retirement_age}\n\n")

    years_to_retirement = retirement_age - age

    if years_to_retirement < 0:
        print("You can already retire... Go do it!")

    else:
        retirement_year = int(date.today().year) + years_to_retirement

        print(f"You have {years_to_retirement} year(s) until you retire")
        print(f"You will retire in {retirement_year}")



if __name__ == '__main__':
    main(sys.argv)
