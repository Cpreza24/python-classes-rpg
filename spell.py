class Spell:
    def __init__(self, name: str, damage: int = 0, effect: str = "", mana_cost: int = 0, cooldown: int = 0):
        """
        Initializes a Spell object.
        :param name: str- The name of the spell.
        :param damage: int - The damage dealt by the spell (default is 0 if the spell does not deal damage).
        :param effect: str- The effect of the spell (e.g., 'burn', 'freeze',"heals 50 HP", "burns for 10 damage",etc.).
        :param mana_cost: int - The mana cost of casting the spell (default is 0 if the spell does not require mana).
        :param cooldown: int - The cooldown period of the spell (default is 0 if the spell can be cast immediately again).
        """
        self.name = name
        self.damage = damage
        self.effect = effect
        self.mana_cost = mana_cost
        self.cooldown = cooldown
        
    def cast(self, target):
        """
        cast the spell on a target.
        """
        if self.damage > 0:
            # Assuming target has a method to take damage
            target.take_damage(self.damage)
            print(f"{target.name} takes {self.damage} damage from {self.name}!")
        if self.effect:
            print(f"{self.name} causes the following effect:{self.effect}")
            
    def __str__(self):
        """
        String representation of the Spell object.
        
        :return: str - Description of the spell
        """
        return f"{self.name}: Damage: {self.damage}, Effect: '{self.effect}', Mana Cost: {self.mana_cost}, Cooldown: {self.cooldown}"
print(Spell_type := Spell("Fireball", 50, "burns for 10 damage", 20, 3))         
            
           