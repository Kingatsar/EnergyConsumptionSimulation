class Household:
    def __init__(self, neededConsumption=0):
        self.neededConsumption = neededConsumption
        self.energyAdded = 0
    
    def getNeededConsumption(self):
        return self.neededConsumption
    
    def setEnergyAdded(self, newEnergyAdded):
        self.energyAdded = newEnergyAdded
    
    def setNeededConsumption(self, newNeededConsumption):
        self.neededConsumption = newNeededConsumption

    