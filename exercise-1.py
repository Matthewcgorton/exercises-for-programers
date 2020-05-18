#!/usr/local/bin/python3
import sys
import unittest


def challenge_0():
    print("challenge 0")

    input_name = input("What is your name? ")
    greeting = "Hello, " + input_name + ", nice to meet you!"
    return greeting


def challenge_1():
    print("challenge 1")

    return("Hello, " + input("What is your name? ") + ", nice to meet you!")


def challenge_2a():
    print("challenge 2a")

    input_name = input("What is your name? ")
    greeting = "Hello, " + input_name + ", nice to meet you!"
    return greeting


def challenge_2b():
    print("challenge 2b - python formating with %s characters")
    print("Hello, " + input("What is your name? ") + ", nice to meet you!")

    print()
    greetings = {"fred": "Good to meet you %s",
                 "kate": "%s, nice to meet you"
                 }

    input_name = input("What is your name? ")

    if input_name.lower() in greetings:
        return greetings[input_name.lower()] % input_name
    else:
        return "Hi " + input_name


def challenge_2c():
    print("challenge 2c - python formatting with {}")
    greetings = {"fred": "Good to meet you {}",
                 "mary": "{}, nice to meet you"
                 }

    input_name = input("What is your name? ")

    if input_name.lower() in greetings:
        return greetings[input_name.lower()].format(input_name)
    else:
        return "Hi " + input_name



if __name__ == '__main__':
    print(challenge_0())
    print(challenge_1())
    print(challenge_2a())
    print(challenge_2b())
    print(challenge_2c())
