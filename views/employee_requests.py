import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "address": "85387 Margarete Ramp",
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "address": "5227 Karley Mission",
        "location_id": 2
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "address": "73082 Barrows Points",
        "location_id": 1
    },
    {
        "name": "Meg Ducharme",
        "address": "477 Damaris Oval",
        "location_id": 2,
        "id": 4
    },
    {
        "name": "Hannah Hall",
        "address": "14602 Schumm Crossroad",
        "location_id": 3,
        "id": 5
    },
    {
        "name": "Emily Lemmon",
        "address": "2067 Abshire Road",
        "location_id": 1,
        "id": 6
    },
    {
        "name": "Jordan Castelloe",
        "address": "42368 Alford River",
        "location_id": 2,
        "id": 7
    },
    {
        "name": "Leah Gwin",
        "address": "997 Jude Haven",
        "location_id": 1,
        "id": 8
    },
    {
        "name": "Caitlin Stein",
        "address": "9480 Sipes Forest",
        "location_id": 2,
        "id": 9
    },
    {
        "name": "Greg Korte",
        "address": "083 Alex Walks",
        "location_id": 3,
        "id": 10
    },
    {
        "name": "Charisse Lambert",
        "address": "14560 Schinner Knoll",
        "location_id": 1,
        "id": 11
    },
    {
        "name": "Madi Peper",
        "address": "04592 Ryan Field",
        "location_id": 2,
        "id": 12
    },
    {
        "name": "Jenna Solis",
        "address": "2456 Norberto Mission",
        "location_id": 1,
        "id": 14
    },
    {
        "name": "Eric \"Macho Man\" Taylor",
        "address": "0209 Harvey Mission",
        "location_id": 3,
        "id": 15
    }
]

def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id,
                l.name location_name,
                l.address location_address
            FROM Employee e
            JOIN Location l
                ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            # Add the dictionary representation of the animal to the list
            employees.append(employee.__dict__)
            
            # Create a location instance from the current row.
            location = Location(row['id'], row['location_name'], row['location_address'])
            
            # Add the dictionary representation of the location to the employee
            employee.location = location.__dict__

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)

# Function with a single parameter
def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return json.dumps(employee.__dict__)
    
def get_employees_by_location(location_id):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from Employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)

def create_employee(new_employee):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id )
        VALUES
            ( ?, ?, ? );
        """, (new_employee['name'], new_employee['address'], new_employee['location_id'] ))
        
        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        
        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee['id'] = id
        
    return json.dumps(new_employee)

# Remove Employee Dictionary from the List
def delete_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

# Replacing Dictionary with New One
def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'],
              new_employee['location_id'], id ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True