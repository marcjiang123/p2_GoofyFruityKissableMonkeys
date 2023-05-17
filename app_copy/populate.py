"""
GoofyFruityKissableMonkeys
"""

from db import *
import csv

# this py populates the database with dataset. MUST have dataset downloaded first

avocado_file = open("avocado_dataset.csv", "r")

#content = avocado_file.read()
#print(content)

contents = csv.reader(avocado_file,  delimiter=',')
#print(contents)

populate(contents)
#populate()
#print(new_content[1].split(",")[0])
