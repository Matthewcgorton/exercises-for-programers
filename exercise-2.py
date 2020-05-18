#!/usr/local/bin/python3
import sys






if __name__ == '__main__':

    input_string = input("pelase enter a string? ")

    if len(input_string) == 0:
        print("No string was entered")
    else:
        print(f"The string is {len(input_string) } characters long")
