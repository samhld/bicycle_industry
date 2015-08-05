import Bicycle
import Shop
import Customer
import random



def makeDrink(boolResponses):
    recipe = []
    for i in boolResponses:
        if boolResponses[i] == True:
            recipe.append(random.choice(ingredients[i]))
    print recipe