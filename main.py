from bikes import Bicycle
from bikes import Shop
from bikes import Customer
import random



myBike = Bicycle("Schwinn", 24, 200)
myBike1 = Bicycle("Torpedo", 24, 200)
myBike2 = Bicycle("Schwinny",30, 250)
myBike3 = Bicycle("Speedy", 20, 100)
myBike4 = Bicycle("Speedy2", 15, 100)
myBike5 = Bicycle("Torpy", 45, 300)

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
        if customer.fund >= shop.pricing(x):
           canAfford.append(x) 
           
    return canAfford 

    
for customer in customers:
    affordList = afford(customer)
    shop.sell(affordList[0])
    print customer.name
