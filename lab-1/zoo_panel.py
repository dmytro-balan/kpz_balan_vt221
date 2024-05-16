from animal_management import Animal
from animal_management import Enclosure
from animal_management import Food
from animal_management import Employee
from animal_management import Inventory



lion = Animal("Льова", "Лев")
tiger = Animal("Тигруля", "Тигор")
enclosure1 = Enclosure("Великий", "Саванна")
enclosure2 = Enclosure("Середній", "Джунглі")
food1 = Food("М’ясо", "100 кг")
food2 = Food("Овочі", "50 кг")
employee1 = Employee("Дмитро Балан", "Прибиральник")
employee2 = Employee("Олег Бондар", "Ветеринар")

inventory = Inventory([lion, tiger], [enclosure1, enclosure2], [food1, food2], [employee1, employee2])
inventory.display_animals()
inventory.display_enclosures()
inventory.display_foods()
inventory.display_employees()