"""
GoofyFruityKissableMonkeys
"""

from db import *

# this py populates the database with dataset. MUST have dataset downloaded first

avocado_file = open("avocado_dataset.csv", "r")
content = avocado_file.read()
#print(content)
new_content = content.split("\n")
for i in range(len(new_content)-1):
    row = new_content[i+1].split(",")
    
#print(new_content[1].split(","))

library = {"average_price":[],
"year":[]
}

