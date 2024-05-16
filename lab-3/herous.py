class Hero:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def equip(self, *items):
        for item in items:
            self.inventory.append(item)

    def show_inventory(self):
        print(f"Inventory of {self.name}:")
        for item in self.inventory:
            if isinstance(item, EquipmentDecorator):
                print(item)
            else:
                print(item.name)


class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hero_class = "Warrior"


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hero_class = "Mage"


class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hero_class = "Paladin"


class EquipmentDecorator(Item):
    def __init__(self, item, modifier):
        super().__init__(item.name)
        self.item = item
        self.modifier = modifier

    def __str__(self):
        return f"{self.item} ({self.modifier})"


class Sword(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Weapon"


class Staff(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Weapon"


class Armor(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Armor"


# Testing the code
if __name__ == "__main__":
    warrior = Warrior("Conan")
    mage = Mage("Gandalf")
    paladin = Paladin("Arthur")

    sword1 = Sword("Excalibur")
    sword2 = Sword("Dragon Slayer")
    staff1 = Staff("Gandalf's Staff")
    staff2 = Staff("Staff of Fire")
    armor1 = Armor("Plate Mail")
    armor2 = Armor("Magic Robe")

    enchanted_sword1 = EquipmentDecorator(sword1, "Enchanted")
    enchanted_sword2 = EquipmentDecorator(sword2, "Legendary")
    magic_staff1 = EquipmentDecorator(staff1, "Magic")
    magic_staff2 = EquipmentDecorator(staff2, "Fire")
    holy_armor1 = EquipmentDecorator(armor1, "Holy")
    holy_armor2 = EquipmentDecorator(armor2, "Arcane")

    warrior.equip(enchanted_sword1, armor1)
    mage.equip(magic_staff1, armor2)
    paladin.equip(holy_armor1, enchanted_sword2)

    warrior.show_inventory()
    mage.show_inventory()
    paladin.show_inventory()
