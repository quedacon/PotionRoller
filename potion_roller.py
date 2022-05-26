import csv
import random

def get_table_data(table):
    data = []
    with open(table) as csvfile:
        reader = csv.reader(csvfile)           
        for row in reader:
            data.append(row)
    return data
    
def get_table_columns(table):
    return len(table[0])

def get_table_rows(table):
    return len(table)

def random_row(table):
    return random.randint(0, get_table_rows(table) - 1)

# if supplied a max column, limits the pick to the left
def random_column(table, max_column = -1):
    col = 0
    max_possible = get_table_columns(table) - 1
    if max_column > max_possible:
        max_column = max_possible
    if max_column > 0:
        col = max_column
    else:
        col = get_table_columns(table) - 1
    return random.randint(0, col)

def random_items_from_table(table: list, number: int):
    items = []
    for _ in range(number):
        rand_row = random_row(table)
        rand_col = random_column(table)
        items.append(table[rand_row][rand_col])
    return items

def generate_potions(number):
    table = get_table_data("Potion_Table.csv")
    rolled_items = random_items_from_table(table, number)
    return rolled_items