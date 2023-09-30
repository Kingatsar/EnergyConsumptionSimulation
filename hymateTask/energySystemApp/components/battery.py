class Battery:
    def __init__(self, capacityMax, batteryID,avalaibleQuantity=0, useBattery=False, storeBattery=True):
        self.capacityMax = capacityMax
        self.avalaibleQuantity = avalaibleQuantity
        self.useBattery = useBattery
        self.batteryID = batteryID
        self.storeBattery = storeBattery

    def getBatteryID(self):
        return self.batteryID

    def getCapacityMax(self):
        return self.capacityMax
    
    def getAvalaibleQuantity(self):
        return self.avalaibleQuantity
    
    def setAvailableQuantity(self, newQuantity):
        self.avalaibleQuantity = min(newQuantity, self.capacityMax)
        self.useBattery = True if self.avalaibleQuantity > 0.2 * self.capacityMax else False
        self.storeBattery = True if self.avalaibleQuantity < self.capacityMax else False

    def canUseBattery(self): 
        return self.useBattery
    
    def canStoreInBattery(self):
        return self.storeBattery
    
    def setUseBattery(self, useBattery):
        self.useBattery = useBattery
    