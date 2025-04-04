class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def swing(self):
        attack = True
        if attack == True:
            print(f'swung the sword')

    def __str__(self):
        return f'{self.name} {self.damage}'

