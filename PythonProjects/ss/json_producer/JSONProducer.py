"""
Created on Aug 27, 2021

@author: Wyatt Meehan

This Python program indefinitely creates JSON files with mexican
restaurant themed random data
"""
import json
import random
import time


# Gets a random menu Item
def get_item():
    items = [("Chicken Burrito", 8.99), ("Veggie Burrito", 7.59), ("House Quesadilla", 8.59), ("Chicken Nachos", 7.99),
             ("Guacamole and Chips", 5.59), ("Taco Salad", 6.99), ("Horchata", 3.99),
             ("Carnitas Huevos Rancheros", 8.99), ("Churros", 4.99), ("Tamales", 7.99)]
    return random.choice(items)


def get_quantity():
    return random.randint(1, 5)


# Produces random JSON Files indefinitely, there is a 2 second wait in between each production
# in order to prevent runaway file generation
def produce():
    json_id = 101
    while True:
        quantity = get_quantity()
        item = get_item()
        json_dict = {
            "ID": json_id,
            "Item": item[0],
            "Price": item[1] * quantity,
            "Qty": quantity
        }
        try:
            json_object = json.dumps(json_dict, indent=3)
            with open("C:/Users/meeha/OneDrive/Desktop/SmoothStack/JSONProducerTests/" + str(json_id) + ".json",
                      "w") as outfile:
                outfile.write(json_object)
        except IOError:
            print("Unable to create File")
        json_id += 1
        time.sleep(2)


if __name__ == '__main__':
    produce()
