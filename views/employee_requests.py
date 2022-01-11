EMPLOYEES = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "address": "85387 Margarete Ramp",
        "manager": "false",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "address": "5227 Karley Mission",
        "manager": "false",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "address": "73082 Barrows Points",
        "manager": "false",
        "locationId": 1
    },
    {
        "name": "Meg Ducharme",
        "address": "477 Damaris Oval",
        "manager": "false",
        "locationId": 2,
        "id": 4
    },
    {
        "name": "Hannah Hall",
        "address": "14602 Schumm Crossroad",
        "manager": "false",
        "locationId": 3,
        "id": 5
    },
    {
        "name": "Emily Lemmon",
        "address": "2067 Abshire Road",
        "manager": "false",
        "locationId": 1,
        "id": 6
    },
    {
        "name": "Jordan Castelloe",
        "address": "42368 Alford River",
        "manager": "false",
        "locationId": 2,
        "id": 7
    },
    {
        "name": "Leah Gwin",
        "address": "997 Jude Haven",
        "manager": "false",
        "locationId": 1,
        "id": 8
    },
    {
        "name": "Caitlin Stein",
        "address": "9480 Sipes Forest",
        "manager": "false",
        "locationId": 2,
        "id": 9
    },
    {
        "name": "Greg Korte",
        "address": "083 Alex Walks",
        "manager": "false",
        "locationId": 3,
        "id": 10
    },
    {
        "name": "Charisse Lambert",
        "address": "14560 Schinner Knoll",
        "manager": "false",
        "locationId": 1,
        "id": 11
    },
    {
        "name": "Madi Peper",
        "address": "04592 Ryan Field",
        "manager": "false",
        "locationId": 2,
        "id": 12
    },
    {
        "name": "Jenna Solis",
        "address": "2456 Norberto Mission",
        "manager": "false",
        "locationId": 1,
        "id": 14
    },
    {
        "name": "Eric \"Macho Man\" Taylor",
        "address": "0209 Harvey Mission",
        "manager": "false",
        "locationId": 3,
        "id": 15
    }
]

def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
        
# Replacing Dictionary with New One
def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break