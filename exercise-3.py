#!/usr/local/bin/python3


if __name__ == '__main__':

    quote = input("what is the quote? ")
    person = input("who said it? ")

    print()
    print(f'{person} says,"{quote}"')
    print()

    quotes = [{"person": "fred", "quote": "Test quote = Fred"},
              {"person": "mary", "quote": "Test quote - Mary"}]

    for quote in quotes:
        print(f"{quote['person']} says, \"{quote['quote']}\"")
