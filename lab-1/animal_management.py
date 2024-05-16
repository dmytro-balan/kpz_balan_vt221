class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Enclosure:
    def __init__(self, size, enclosure_type):
        self.size = size
        self.enclosure_type = enclosure_type

class Food:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
class Inventory:
    def __init__(self, animals, enclosures, foods, employees):
        self.animals = animals
        self.enclosures = enclosures
        self.foods = foods
        self.employees = employees

    def display_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(f"Name: {animal.name}, Species: {animal.species}")

    def display_enclosures(self):
        print("\nEnclosures in the zoo:")
        for enclosure in self.enclosures:
            print(f"Size: {enclosure.size}, Type: {enclosure.enclosure_type}")

    def display_foods(self):
        print("\nFood available in the zoo:")
        for food in self.foods:
            print(f"Name: {food.name}, Quantity: {food.quantity}")

    def display_employees(self):
        print("\nEmployees in the zoo:")
        for employee in self.employees:
            print(f"Name: {employee.name}, Position: {employee.position}")


def display_enclosures(self):
    print("\nEnclosures in the zoo:")
    for enclosure in self.enclosures:
        print(f"Size: {enclosure.size}, Type: {enclosure.enclosure_type}")


def display_foods(self):
    print("\nFood available in the zoo:")
    for food in self.foods:
        print(f"Name: {food.name}, Quantity: {food.quantity}")


def display_employees(self):
    print("\nEmployees in the zoo:")
    for employee in self.employees:
        print(f"Name: {employee.name}, Position: {employee.position}")