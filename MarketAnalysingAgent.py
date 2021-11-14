"""
Created by Vineeth Menon M

"""

import numpy as np
import random

class Environment(object):
    def __init__(self):
        # Generate 5 days random date price of sugar
        self.priceOfPrevious5Days = np.random.randint(30,40,5)
        print("Previous 5 days' rates", self.priceOfPrevious5Days)
        # Amount of Sugar Purchased, Amount remaining, Amount used
        self.maxInventory = 100
        self.sugarInventory = 100 # Assuming that there is a threshold at the beginning of the week
        self.sugarConsumed = 0 # No usage during initialisation
        self.criticalNumber  = 30 # Amount to maintain
        self.buyNumber = 50 # Amount after which the agent can buy

class MarketAnalysisAgent(Environment):
    def __init__(self, environment):
        env.sugarConsumed = np.random.randint(0,80) # Assumes today's consumption
        print("Today's consumption: ", env.sugarConsumed)
        self.rateToday = random.randint(30,40)
        print("Rate today: ", self.rateToday)
        self.last5DayAvg = sum(env.priceOfPrevious5Days)/len(env.priceOfPrevious5Days)
        print("Average of last 5 days market: ", self.last5DayAvg)
        env.sugarInventory = env.sugarInventory - env.sugarConsumed
        print("Current Inventory: ", env.sugarInventory)

        self.minamountToBuy = env.criticalNumber - env.sugarInventory
        self.maxamountToBuy = env.maxInventory - env.sugarInventory
        print("Minimum Sugar to buy: ", self.minamountToBuy)
        print("Maximum Sugar to buy: ", self.maxamountToBuy)

        """
        Buying decision: 
        1. If the amount is <= critical number and also if todays rate is less than average of last 5 days.
        2. If amount<= critical number and and todays rate is greater, purchase minimum to get it to critical number. 
        3. Else if amount > critical number, skip. 
        
        """
        if(env.sugarInventory <= env.criticalNumber and self.rateToday <= self.last5DayAvg):
            print("\nBuying max capacity:", self.maxamountToBuy)
        elif(env.sugarInventory <= env.criticalNumber and self.rateToday > self.last5DayAvg):
            if(self.minamountToBuy > 0):
                print("\nBuying to reach critical number: ", self.minamountToBuy)
        else:
            print("\nWe are at a safe inventory status, So no buy!")

env = Environment()
MAA = MarketAnalysisAgent(env)