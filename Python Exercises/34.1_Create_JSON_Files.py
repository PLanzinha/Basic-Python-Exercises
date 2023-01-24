# Exercise 34 needs a JSON file lets create one here

import json


birthday_info = {
    "Isaac Newton": "04/01/1643",
    "Albert Einstein": "14/03/1879",
    "Marie Curie": "07/11/1867",
    "Stephen Hawking": "01/08/1942"
}

filename = "scientists.json"

with open(filename, "w") as json_file:
    json.dump(birthday_info, json_file)

