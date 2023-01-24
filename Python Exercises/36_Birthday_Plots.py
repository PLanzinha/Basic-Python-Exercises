# Exercise 36 - Birthday Plots

# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
#
# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays
# in! Because it would take a long time for you to input the months of various scientists, you can use my scientist
# birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or
# its solution) and draw your histogram.
#
# If you are using a purely web-based interface for coding, this exercise won’t work for you, since it requires
# installing the bokeh Python package. Now might be a good time to install Python on your own computer.

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


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

        return year_months, month_counts


def visualise_months():
    year_months, month_counts = birthday_months()
    months = list(year_months.values())  # Use month names as x-axis labels
    counts = [month_counts.get(month_number, 0) for month_number in year_months.keys()]

    output_file("birthday_months.html")
    p = figure(x_range=months, height=350, title="Birthday Months",
               toolbar_location=None, tools="")

    p.vbar(x=months, top=counts, width=0.9)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    show(p)


if __name__ == "__main__":
    birthday_months()
    visualise_months()
