class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
    def __repr__(self): 
        return "Bicycle(%r, %r, %r)" % (self.name, self.weight, self.cost)
    
class Shop(object):

    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.markup = 1.20
        
    def addInventory(self, bike):
        self.inventory.append(bike)
        
    def sell(self, cost, price):
        margin = price - cost
        return margin
    
    
    # def totalProfit(self, margin):
    #     profit = 0
    #     for x in self.sales:
    #         profit += margin
class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    
    def buy(self):
        pass
            
myBike = Bicycle("Schwinn", 24, 200)
myBike1 = Bicycle("Torpedo", 24, 200)

shop = Shop("Sam's Bikes", [myBike,myBike1])

shop.addInventory([myBike, myBike1])
print shop.inventory