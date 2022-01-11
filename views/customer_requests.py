CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "address": "002 Smitham Trail",
        "vip_customer": "false",
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Emma Beaton",
        "address": "590 Tia Throughway",
        "vip_customer": "false",
        "location_id": 2
    },
    {
        "id": 3,
        "name": "Dani Adkins",
        "address": "903 Thea Coves",
        "vip_customer": "false",
        "location_id": 1
    },
    {
        "id": 4,
        "name": "Adam Oswalt",
        "address": "80019 Weimann Falls",
        "vip_customer": "false",
        "location_id": 2
    },
    {
        "id": 5,
        "name": "Fletcher Bangs",
        "address": "925 Jillian Motorway",
        "vip_customer": "false",
        "location_id": 3
    },
    {
        "id": 6,
        "name": "Angela Lee",
        "address": "9948 Jennings Plain",
        "vip_customer": "false",
        "location_id": 1
    },
    {
        "name": "mike mike",
        "address": "6504 Jackie Curve",
        "vip_customer": "false",
        "location_id": 2,
        "id": 7
    }
]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
        
# Replacing Dictionary with New One
def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break