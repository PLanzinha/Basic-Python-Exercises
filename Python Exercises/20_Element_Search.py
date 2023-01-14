# Exercise 20 - Element Search

# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 22, 25, 36, 49, 64, 81, 100]

def ele_search(find_element):

    for element in a:
        if element == find_element:
            return True
    return False


if __name__ == "__main__":
    find_element = int(input("Please write a number from 1 to 100 to see if its inside the list.\n"))
    result = ele_search(find_element)
    if result == False:
        print(f"It's {result}, {find_element} is not in the list, please try again!")
    else:
        print(f"It's {result}, Congratulations {find_element} is in the list! ")
