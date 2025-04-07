class Attack:
    """
    A class to represent an attack in a game.
    """

    def __init__(self, name: str, damage: int, special_effect:str=None):
        """
        Initializes the attack with a name and damage value.

        :param name: The name of the attack.
        :param damage: The damage dealt by the attack.
        """
        self.name = name
        self.damage = damage
        self.special_effect = special_effect
    
    def describe(self):
        """ Returns a human-readable description of the attack."""  
        if self.special_effect:
            return f"{self.name} deals {self.damage} damage with a special effect: {self.special_effect}." 
        else:
            return f"{self.name} deals {self.damage} damage." 
        
    def __repr__(self):
        return f"Attack(name='{self.name}', damage={self.damage})"
    
# Example usage
if __name__ == "__main__":
    fireball = Attack("Fireball", 50, "burns for 10 damage")
    print(fireball.describe())  # Output: Fireball deals 50 damage with a special effect: burns for 10 damage.
    
    punch = Attack("Punch", 10)
    print(punch.describe())  # Output: Punch deals 10 damage.
    
    print(repr(fireball))  # Output: Attack(name='Fireball', damage=50)
    
# Example usage
bite = Attack("Bite", 15, "infects with a virus")
print(bite.describe())  # Output: Bite deals 15 damage with a special effect: infects with a virus.

slash = Attack("Quick Slash", 10)
print(slash.describe())  # Output: Quick Slash deals 10 damage.