"""
GoofyFruityKissableMonkeys
"""

from db import *

# this py populates the database with dataset. MUST have dataset downloaded first

avocado_file = open("avocado_dataset.csv", "r")
content = avocado_file.read()
#print(content)

def populate():
    new_content = content.split("\n")
    for i in range(len(new_content)-1):
        values = new_content[i+1].split(",")
        table = get_column_names()
        for i in range(len(values)-1):
            table_insert(table[i], values[i])

#populate()
#print(new_content[1].split(",")[0])
