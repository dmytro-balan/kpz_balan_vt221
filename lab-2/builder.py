class Hero:
    def __init__(self):
        self.height = None
        self.build = None
        self.hair_color = None
        self.eye_color = None
        self.outfit = None
        self.inventory = None

    def __str__(self):
        return f"Hero: height={self.height}, build={self.build}, hair_color={self.hair_color}, " \
               f"eye_color={self.eye_color}, outfit={self.outfit}, inventory={self.inventory}"


class HeroBuilder:
    def __init__(self):
        self.hero = Hero()

    def set_height(self, height):
        self.hero.height = height
        return self

    def set_build(self, build):
        self.hero.build = build
        return self

    def set_hair_color(self, hair_color):
        self.hero.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.hero.eye_color = eye_color
        return self

    def set_outfit(self, outfit):
        self.hero.outfit = outfit
        return self

    def set_inventory(self, inventory):
        self.hero.inventory = inventory
        return self

    def build(self):
        return self.hero


class EnemyBuilder(HeroBuilder):
    def __init__(self):
        super().__init__()

    def set_evil_deeds(self, evil_deeds):
        self.hero.evil_deeds = evil_deeds
        return self

    def set_good_deeds(self, good_deeds):
        self.hero.good_deeds = good_deeds
        return self


class Director:
    @staticmethod
    def create_hero(builder):
        return builder.set_height(180) \
                      .set_build("Athletic") \
                      .set_hair_color("Blonde") \
                      .set_eye_color("Blue") \
                      .set_outfit("Heroic Armor") \
                      .set_inventory("Sword") \
                      .build()

    @staticmethod
    def create_enemy(builder):
        return builder.set_height(170) \
                      .set_build("Muscular") \
                      .set_hair_color("Black") \
                      .set_eye_color("Red") \
                      .set_outfit("Dark Armor") \
                      .set_inventory("Dagger") \
                      .set_evil_deeds(["Plundering", "Terrorizing"]) \
                      .set_good_deeds(["None"]) \
                      .build()


hero_builder = HeroBuilder()
enemy_builder = EnemyBuilder()

hero = Director.create_hero(hero_builder)
enemy = Director.create_enemy(enemy_builder)

print(hero)
print(enemy)
