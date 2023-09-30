
from energySystemApp.components.battery import Battery
from energySystemApp.components.cleanEnergy import CleanEnergy

class EnergyManager:
    
    def __init__(self, producingEnergiesNumber, batteryStockageNumber, maxBatteryCapacity, grid, household, time=0):
        self.producingEnergies = self.createProducingEnergiesDict(producingEnergiesNumber)
        self.batteryStockage = self.createBatteryStockageDict(batteryStockageNumber, maxBatteryCapacity)

        self.grid = grid
        self.household = household
        self.time = time


    def createProducingEnergiesDict(self, producingEnergiesNumber):
        producingEnergies = {}
        for i in range(producingEnergiesNumber):
            producingEnergies[f"myEnergy{i}"] = CleanEnergy(currentEnergy=0, energyID=f"myEnergy{i}")
        return producingEnergies
    
    def createBatteryStockageDict(self, batteryStockageNumber, maxBatteryCapacity):
        batteryStockage = {}
        for i in range(batteryStockageNumber):
            batteryStockage["myBattery"+str(i)+""] = Battery(capacityMax=maxBatteryCapacity, batteryID=f"myBattery{i}", avalaibleQuantity=0, useBattery=False, storeBattery=True)
        return batteryStockage

    def getProducingEnergies(self):
        return self.producingEnergies
    
    def getBatteryStockage(self):
        return self.batteryStockage
    
    def getGrid(self):
        return self.grid
    
    def getHousehold(self):
        return self.household
    
    def getGridConsumption(self):
        return self.grid.getGridConsumption()

    def getTotalBatteryAvailablestorage(self):
        totalBatteryEnergyAvailable = 0
        for batteryObject in self.batteryStockage.values():
            totalBatteryEnergyAvailable += (batteryObject.getCapacityMax() - batteryObject.getAvalaibleQuantity())  
        return totalBatteryEnergyAvailable
    
    def getTotalBatteryEnergyAvailable(self):
        totalBatteryEnergyAvailable = 0
        for batteryObject in self.batteryStockage.values():
            totalBatteryEnergyAvailable += batteryObject.getAvalaibleQuantity()
        return totalBatteryEnergyAvailable

    def getTotalCleanEnergy(self):
        totalCleanEnergy = 0
        for cleanEnergyObject in self.producingEnergies.values():
            totalCleanEnergy += cleanEnergyObject.getCurrentEnergy()
        return totalCleanEnergy
    
    def getTotalStoredCleanEnergy(self):
        totalStoredCleanEnergy = 0
        for batteryObject in self.batteryStockage.values():
            totalStoredCleanEnergy += batteryObject.getAvalaibleQuantity()
        return totalStoredCleanEnergy
    
    def getTotalConsumption(self):
        return self.household.getNeededConsumption()
    
    def getNeededCleanEnergy(self):
        return self.getTotalConsumption() - self.getTotalCleanEnergy()
    
    def updateCleanEnergy(self, newCurrentEnergy):
        for cleanEnergyID in self.producingEnergies.keys():
            self.producingEnergies[cleanEnergyID].setCurrentEnergy(newCurrentEnergy)
    
    def updateHouseholdNeeds(self, newHouseholdNeeds):
        self.household.setNeededConsumption(newHouseholdNeeds)
    
    def updateHouseholdEnergyAdded(self, newEnergyAdded):
        self.household.setEnergyAdded(newEnergyAdded)

    def updateBattery(self, batteryID, newQuantity):
        self.batteryStockage[batteryID].setAvailableQuantity(newQuantity)
    
    def updateGrid(self, newGridConsumption):
        value = self.grid.getGridConsumption() + newGridConsumption
        self.grid.setGridConsumption(value)

    def retrieveValuesFromComponents(self):
        solarEnergyLeft = self.getTotalCleanEnergy()/1000
        batteryEnergyAvailable = self.getTotalBatteryEnergyAvailable()/1000
        gridConsumption = self.getGridConsumption()

        return solarEnergyLeft, batteryEnergyAvailable, gridConsumption

    def giveEnergy(self):
        energyNeedClean = self.getTotalCleanEnergy() - self.household.getNeededConsumption() 
        energyNeedStored = self.getTotalStoredCleanEnergy() - self.household.getNeededConsumption()
        if energyNeedClean >= 0:
            self.updateHouseholdEnergyAdded(self.household.getNeededConsumption())
            self.updateHouseholdNeeds(0)
            energyToStoreAvailable = self.getTotalBatteryAvailablestorage()
            if energyNeedClean > 0 and energyToStoreAvailable > 0:
                for batteryId, batteryObject in self.batteryStockage.items():
                    if batteryObject.storeBattery:
                        # store energy in battery
                        if (energyNeedClean <= 0) or (energyToStoreAvailable <= 0):
                            break
                        else:
                            batteryEnergyAvailable = batteryObject.getCapacityMax() - batteryObject.getAvalaibleQuantity()
                            energyToStore = min(batteryEnergyAvailable,energyNeedClean)
                            self.batteryStockage[batteryId] .setAvailableQuantity(energyToStore)
                            
                            energyNeedClean -= energyToStore
                            energyToStoreAvailable -= energyToStore

        elif energyNeedStored >=0 : 
            self.updateHouseholdNeeds(0)
            energyToUseAvailable = self.getTotalStoredCleanEnergy()
            if energyNeedStored > 0 and energyToUseAvailable > 0:
                for batteryId, batteryObject in self.batteryStockage.items():
                    if batteryObject.canUseBattery():
                        # use energy from battery
                        if (energyNeedStored <= 0) or (energyToUseAvailable <= 0):
                            break
                        else:
                            batteryEnergyAvailable = batteryObject.getAvalaibleQuantity()
                            energyToUse = min(batteryEnergyAvailable,energyNeedStored)
                            self.batteryStockage[batteryId].setAvailableQuantity(energyToUse)
                            energyNeedStored -= energyToUse
                            energyToUseAvailable -= energyToUse
        
        else:
            self.updateGrid(-1*self.household.getNeededConsumption())
            self.updateHouseholdNeeds(0)


                        
                   



