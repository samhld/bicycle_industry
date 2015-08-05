class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def __repr__(self): 
        return "Bicycle(%r, %r, %r)" % (self.name, self.weight, self.cost)
    
class Shop(object):

    def __init__(self):
        self.markup = 1.20
      
    inventory = []    
    def addInventory(self, bike):
        self.inventory.append(bike)
        
    def pricing(self, bicycle):
        price = bicycle.cost * self.markup
        return price
        
    def sell(self, bicycle):
        profit = self.pricing(bicycle) - bicycle.cost
        print "profit is {}".format(profit)
    
    
    # def totalProfit(self, margin):
    #     profit = 0
    #     for x in self.sales:
    #         profit += margin
class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bikes = []
    
    def buy(self, bike):
        self.bikes.append(bike)
            
