import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "address": "002 Smitham Trail",
        "email": "Ryan@Tanay.com",
        "password": "password"
    },
    {
        "id": 2,
        "name": "Emma Beaton",
        "address": "590 Tia Throughway",
        "email": "Emma@Beaton.com",
        "password": "password"
    },
    {
        "id": 3,
        "name": "Dani Adkins",
        "address": "903 Thea Coves",
        "email": "Dani@Adkins.com",
        "password": "password"
    },
    {
        "id": 4,
        "name": "Adam Oswalt",
        "address": "80019 Weimann Falls",
        "email": "Adam@Oswalt.com",
        "password": "password"
    },
    {
        "id": 5,
        "name": "Fletcher Bangs",
        "address": "925 Jillian Motorway",
        "email": "Fletcher@Bangs.com",
        "password": "password"
    },
    {
        "id": 6,
        "name": "Angela Lee",
        "address": "9948 Jennings Plain",
        "email": "Angela@Lee.com",
        "password": "password"
    },
    {
        "name": "Emily Lemon",
        "address": "6504 Jackie Curve",
        "email": "Emily@Lemon.com",
        "password": "password",
        "id": 7
    }
]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)

# Function with a single parameter
def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

        return json.dumps(customer.__dict__)
    
def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

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

# Remove Customer Dictionary from the List
def delete_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))
        
# Replacing Dictionary with New One
def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break