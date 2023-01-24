# Exercise 33 - Birthday Dictionaries

# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information
# based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should
# ask the user to enter a name, and return the birthday of that person back to them.

friends_birthday = [
    {
        "George": '11/06/1998'
    },
    {
        "Alice": '23/02/1995'
    },
    {
        "Alvie": '30/10/1995'
    },
    {
        "Charlotte": '10/10/1996'
    }
]


def birthday_friend(n):
    birthday_dic = {
        "George": '11/06/1998',
        "Alice": '23/02/1995',
        "Alvie": '30/10/1995',
        "Charlotte": '10/10/1996'
    }
    print(birthday_dic[n])


if __name__ == "__main__":
    birthday_input = input("Please write the name of the friend you want to know the birthday of.\n").capitalize()
    birthday_friend(birthday_input)
