class CleanEnergy:
    def __init__(self, energyID, currentEnergy ):
        self.energyID = energyID
        self.currentEnergy  = currentEnergy 
    
    def getCleanEnergyID(self):
        return self.energyID

    def getCurrentEnergy (self):
        return self.currentEnergy 
    
    def setCurrentEnergy(self, newCurrentEnergy):
        self.currentEnergy = newCurrentEnergy



    