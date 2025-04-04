class potion():
    def __init__(self,name:str, potion_type, effect: str, potency: int, duration: int = 0):
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

    def __str__(self):
        """
        String representation of the potion.
        
        :return: str - Description of the potion
        """
        return f"{self.name}: {self.effect}"