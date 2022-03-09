# Start with the code in a given example
#
# Add two more features:
#
# 1. a way for the user to focus the query on one or more selected keywords
# 2. improved output for the query results
# Upload your improved code as a .py file for testing.


import requests
import json

categories_response = requests.get("https://api.publicapis.org/categories")
val = json.dumps(categories_response.json())
val1 = json.loads(val)

selection = 0
while selection < 1 or selection > 2:
    selection = input("""
        Please choose an option from the menu below:\n
        1 - Search APIs by Category
        2 - Some random API
        """)
    selection = int(selection)

if selection == 1:
    categories = val1["categories"]
    txt = ", "
    cat_str = txt.join(categories)
    print("Here are the categories to choose from:\n" + cat_str)
    choice = ""
    while not choice in categories:
        choice = input("Please input a category from the list: ")
    response = requests.get("https://api.publicapis.org/entries?category=" + choice)
else:
    response = requests.get("https://api.publicapis.org/random")

def jprint(obj):
    # create a formatted string of the Python JSON object
    print("+++++++++ API +++++++++")
    val = json.dumps(obj)
    val1 = json.loads(val)
    for entry in val1["entries"]:
        print("--------------------")
        for key in val1["entries"][0]:
            print(key, ": " + str(val1["entries"][0][key]))

jprint(response.json())
