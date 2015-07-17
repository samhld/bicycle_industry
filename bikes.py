class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
class Shop(object):
    inventory = []
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        return inventory
    # def sell(Bicycle.cost, price):
    #     margin = price - Bicycle.cost
    #     return margin
    
    
    # def totalProfit(margin):
    #     profit
    #     for x in sales:
    #         profit += margin
            
            
myBike = Bicycle("Schwinn", 24, 200)
print myBike.name
print Shop.inventory