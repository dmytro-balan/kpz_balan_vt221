import copy
class Virus:
    def __init__(self, weight, age, name, species):
        self.weight = weight
        self.age = age
        self.name = name
        self.species = species
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def clone(self):
        return copy.deepcopy(self)

first_generation_virus = Virus(10, 1, "First Virus", "first")
second_generation_virus = Virus(12, 2, "Second Virus", "second")
third_generation_virus = Virus(15, 3, "Third Virus", "third")

first_generation_virus.add_child(second_generation_virus)
second_generation_virus.add_child(third_generation_virus)

cloned_virus = first_generation_virus.clone()

print(cloned_virus.name)
print(cloned_virus.children[0].name)
print(cloned_virus.children[0].children[0].name)
