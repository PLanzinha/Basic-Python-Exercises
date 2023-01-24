# Exercise 34 - Birthday Json
import json
# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your
# program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary
# defined in the program.
#
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file
# you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names,
# your JSON file should keep getting bigger and bigger.

import json


def read_json(name):
    with open("scientists.json", "r") as open_json:
        dictionary_data = json.load(open_json)

        if name in dictionary_data:
            print(f"The birthday of {name} was found.")
            return dictionary_data[name]
        else:
            return f"Try again, the name {name} was not found in dictionary."


def add_to_dic(name, birthday):
    with open("scientists.json", "r") as open_json:
        new_info = json.load(open_json)

    new_info[name] = birthday

    with open("scientists.json", "w") as dump_json:
        json.dump(new_info, dump_json)


if __name__ == "__main__":
    name_input = input("Please write the name of the scientist you want to know the birthday of:\n")
    birthday = read_json(name_input)
    print(birthday)

    add_name = str(input("Enter a new name to add to the dictionary.\n"))
    add_birthday = input("Enter the birthday of the new name entry, in this format: dd/mm/yyyy\n")
    add_to_dic(add_name, add_birthday)
