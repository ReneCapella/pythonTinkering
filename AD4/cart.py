


import json
import os.path
##################################################################
# Order Class
class Order:
    order = {}

    def __init__(self, order_id, customer_id, products):
        self.order = {
        "order_id" : order_id,
        "customer_id" : customer_id,
        "products" : products
        }

    def get_order(self):
        return self.order

    def get_order_id(self):
        return self.order["order_id"]


    def set_total(self, total_cost):
        self.order["order_total"] = total_cost

    def set_products(self, products):
            self.order["products"] = products


    def ouput_json(self):
        string_filename = str(self.order["order_id"]) + ".json"
        json_string = json.dumps(self.order)

        json_file = open(string_filename, 'w')
        json_file.write(json_string)
        json_file.close()


##################################################################
# Menu
selection = 0
while selection < 1 or selection > 2:
    selection = input("""
\tPlease choose an option from the menu below:\n
\t1 - Enter one or more orders
\t2 - Search for an order
        """)
    print("\n")
    selection = int(selection)

##################################################################
# Actions
if selection == 1:
    count = 0

    order_count = input("How many orders today?")
    # loop for the given amount of orders
    for number in range(int(order_count)):
        count += 1
        print("Order # ", count, " of ", order_count)

        products = {}
        customer_id   = input("Customer ID: ")
        order = Order(count, customer_id, products)
        finished_entering = False
        number = 0

        while not finished_entering:
            number        += 1
            p_count       = number
            product_id    = input("Product ID: ")
            product_no    = input("Product Count: ")
            product_name  = input("Product Name: ")
            product_price = input("Product Price: ")

            # Create Dictionarys
            products["prod" + str(p_count)] = {"product_id" : product_id,
                                                "product_no," : product_no,
                                                "product_name," : product_name,
                                                "product_price," : product_price
                                                }
            p_count += 1

            finished = ''
            while finished != "Y" and finished != "N":
                finished = input("Are you finished entering prodects for this order? Y/N ")
            if finished == 'Y':
                finished_entering = True

        # Set all the products
        order.set_products(products)
        # Print order to json file
        order.ouput_json()
elif selection == 2:
    order_found = False
    while not order_found:
        order_id_to_find = input("Please provide the Order ID: ")
        if os.path.exists(order_id_to_find + ".json"):
            order_found = True
        else:
            print("We do not have an order matching that Order ID")

    # Print the file to the terminal
    file = open(order_id_to_find + ".json", "r")
    for x in file:
        parsed = json.loads(x)
        print(json.dumps(parsed, indent=4, sort_keys=True))
