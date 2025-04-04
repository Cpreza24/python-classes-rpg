class shop():
    def __init__(self):
        self.inventory = {}
        self.balance = 0.0
    def buy(self, item, quantity, price):
        total_cost = quantity * price
        if total_cost > self.balance:
            print (f'Not enough balance to buy {quantity} units of {item}.')
        else:
            self.balance -= total_cost
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"Bough {quantity} units of {item}. Total cost: ${total_cost:.2f} ")
    def sell(self, item, quantity, price):
        if item not in self.inventory or self.inventory[item] < quantity:
            print(f"Not enough {item} in inventory to sell.")
        else:
            total_revenue = quantity * price
            self.balance += total_revenue
            self.inventory[item] -= quantity
            print(f"Sold {quantity} unit of {item}. Total revenue: ${total_revenue:.2f}")
    def __str__(self):
        return f"Inventory: {self.inventory}\nBalance: ${self.balance:.2f}"
