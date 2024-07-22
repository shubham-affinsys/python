persons = [
    {
        "name": "John Doe",
        "age": 30,
        "address": {
            "city": "New York",
            "zipcode": "10001",
            "state": "NY"
        },
        "contacts": [
            {"type": "email", "value": "john.doe@example.com"},
            {"type": "phone", "value": "+123456789"}
        ]
    },
    {
        "name": "shubh",
        "age": 25,
        "address": {
            "city": "San Francisco",
            "zipcode": "94105",
            "state": "CA"
        },
        "contacts": [
            {"type": "email", "value": "alice.smith@example.com"},
            {"type": "phone", "value": "+987654321"}
        ]
    }
]


def greet(person):
    print(f"hello {person['name']}")

def name(person):
    return person['name']

def contacts(person):
    return f"email: {person['contacts'][0]['value']}, phone: {person['contacts'][1]['value']}"

def age(person):
    return person['age']

def address(person):
    return f"city: {person['address']['city']}, zipcode: {person['address']['zipcode']}, state: {person['address']['state']}"

def details(person):
    return f"Name: {name(person)} \nage: {age(person)} \ncontacts: {contacts(person)} \naddress: {address(person)}\n"
