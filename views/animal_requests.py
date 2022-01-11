ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    },
    {
        "id": 4,
        "name": "Doodles",
        "species": "German Shepherd",
        "locationId": 1,
        "customerId": 15
    },
    {
        "id": 5,
        "name": "Angus",
        "species": "Dalmatian 👾",
        "locationId": 1,
        "customerId": 16
    },
    {
        "id": 6,
        "name": "Henley",
        "species": "Carolina Retriever 🚒",
        "locationId": 1,
        "customerId": 17
    },
    {
        "id": 7,
        "name": "Derkins",
        "species": "Shih tzu 👿",
        "locationId": 2,
        "customerId": 18
    },
    {
        "id": 8,
        "name": "Checkers",
        "species": "Bulldog",
        "locationId": 1,
        "customerId": 19
    },
    {
        "name": "Sawyer",
        "species": "Lollie",
        "id": 9,
        "locationId": 2,
        "customerId": 20
    },
    {
        "name": "Gypsy",
        "species": "Miniature Schnauzer",
        "id": 10,
        "locationId": 1,
        "customerId": 21
    },
    {
        "name": "Zipper",
        "species": "Terrier",
        "locationId": 2,
        "customerId": 22,
        "id": 11
    },
    {
        "name": "Blue",
        "species": "Hound dog",
        "locationId": 2,
        "customerId": 16,
        "id": 12
    },
    {
        "name": "Bugle",
        "species": "Beagle",
        "locationId": 1,
        "customerId": 17,
        "id": 13
    }
]

def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal