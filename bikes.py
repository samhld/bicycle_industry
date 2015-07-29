class Bicycle(object):
    def __init__(self, name, weight, cost, price):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.price = price
    def __repr__(self): 
        return "Bicycle(%r, %r, %r)" % (self.name, self.weight, self.cost)
    
class Shop(object):

    def __init__(self):
        self.markup = 1.20
      
    inventory = []    
    def addInventory(self, bike):
        self.inventory.append(bike)
        
    def sell(self, cost, price):
        self.price = cost * self.markup
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
        self.bikes = []
    
    def buy(self, bike):
        self.bikes.append(bike)
            

myBike = Bicycle("Schwinn", 24, 200, 250)
myBike1 = Bicycle("Torpedo", 24, 200, 300)
myBike2 = Bicycle("Schwinny",30, 250, 350)
myBike3 = Bicycle("Speedy", 20, 100, 175)
myBike4 = Bicycle("Speedy2", 15, 100, 150)
myBike5 = Bicycle("Torpy", 45, 300, 500)

bicycles = [myBike,myBike1,myBike2,myBike3,myBike4,myBike5]

shop = Shop()

shop.addInventory([myBike,myBike1,myBike2,myBike3,myBike4,myBike5])

bill = Customer("Bill", 200)
sam = Customer("Sam", 500)
jared = Customer("Jared", 1000)

customers = [bill,sam,jared]


def afford(customer):
    canAfford = []
    for x in bicycles:
        if customer.fund >= x.price:
           canAfford.append(x) 
           
    return canAfford 
    
    
# def afford(customer):
#     canAfford = []
#     for x in range(len(bicycles)):
#         if customer.fund >= bicycles[x].price:
#           canAfford.append(bicycles[x])           
#    return canAfford
    

    
print afford(sam)

