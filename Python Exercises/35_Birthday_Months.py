# Exercise 35 - Birthday Months

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this
# exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists
# have a birthday in each month.
import json
from collections import Counter


def birthday_months():
    year_months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    with open("scientists.json", "r") as open_json:
        info = json.load(open_json)

        json_months = []

        for date in info.values():
            month = date.split('/')[1]
            json_months.append(month)

        month_counts = Counter(json_months)

        for month_number, count in month_counts.items():
            month_name = year_months.get(month_number)
            print(f"For the month of {month_name} there are {count} birthdays in the dictionary.")


if __name__ == "__main__":
    birthday_months()

