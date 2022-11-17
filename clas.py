class Hero:
    abyliti=True
    def __init__(self, name):
        self.name=name

class Hero_super(Hero):
    def __init__(self, name):
        super().__init__(name)
    def name_hero(self):
        print(f"{self.name} it is super hero")
    def __str__(self):
        return f"{self.name} it is super hero"

hero=Hero_super('alihan')
hero.name_hero()