# Exercise 22 - Read From File

# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra: Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
# and count how many of each “category” of each image there are. This text file is actually a list of files
# corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the
# images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene
# category.

"""''
with open('scrap.txt', 'r', encoding='utf-8') as open_file:
    all_text = open_file.read()

print(all_text)


with open('training_01.txt', 'r') as open_file:
    line = open_file.read()
    while line:
        print(line)
        line = open_file.read()
''"""


count_cat = {}

with open('training_01.txt', 'r') as open_file:
    for line in open_file:
        i = line.replace("_", " ").split('/')
        if len(i) >= 2:
            item = i[-2]
            if item in count_cat:
                count_cat[item] += 1
            else:
                count_cat[item] = 1

for category, count in count_cat.items():
    print(f"The {category} category has {count} files associated.")


