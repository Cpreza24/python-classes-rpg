class Potion:
    def __init__(self, name:str, potion_type, effect: str, potency: int, duration: int = 0):
        """
        Initializes a Potion object.
        :param name: str - The name of the potion.
        :param potion_type: The type of the potion (e.g., 'healing', 'buff', etc.)
        :param effect: str- The effect of the potion (e.g., 'heals 50 HP', 'increases strength by 10', etc.)
        :param potency: int- The strength or potency of the potion (e.g., how much it heals or buffs).
        :param duration: int - Duration of the effect (0 for instant effects like healing.

        """
        self.name = name
        self.potion_type = potion_type
        self.effect = effect
        self.potency = potency
        self.duration = duration 
        
    def use(self, target):
        """ Applies the potion's effect to a target.
        :param target: The entity using or receiving the potion's effect."""
            
        if self.potion_type == "healing":
            target.heal(self.potency)
            print(f"{target.name} has been healed for {self.potency} HP!")
        else:
            target.apply_buff(self.effect, self.potency, self.duration)
            print(f"{target.name} has received for {self.potency} with effect '{self.effect}.'")
            

    def __str__(self):
        """
        String representation of the potion.
        
        :return: str - Description of the potion
        """
        return f"{self.name}: {self.effect} (Potency: {self.potency}, Duration: {self.duration})"
    
Potion_type = Potion("Health Potion", "healing", "heals 50 HP", 50)
print(Potion_type)  # This will print the string representation of the Potion object
print(Potion_type := Potion("Health Potion", "healing", "heals 50 HP", 50))
