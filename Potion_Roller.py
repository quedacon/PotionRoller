import csv
import random
import webbrowser

number_of_rows = 0
number_of_columns = 3

table_data = []

with open("Potion_Table.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        table_data.append(row)
        number_of_rows += 1

def get_random_row():
    return random.randint(0, number_of_rows - 1)
def get_random_col():
    return random.randint(0, number_of_columns - 1)

number_of_rolls = 32
rolls = []
for _ in range(number_of_rolls):
    rand_row = get_random_row()
    rand_col = get_random_col()
    rolls.append(table_data[rand_row][rand_col])

f = open("PotionRoller.html", "w")

html_opener = """
<html>
<head>
<title>Potion Roller</title>
</head>
<body>
<p>You found the following treasure: </p>
<p>
"""

html_closer = """
</p>
</body>
</html>
"""

content = ""

for roll in rolls:
    content += "<li>" + str(roll) + "</li>"

new_page = html_opener + content + html_closer

f.write(new_page)
f.close()

webbrowser.open("PotionRoller.html")