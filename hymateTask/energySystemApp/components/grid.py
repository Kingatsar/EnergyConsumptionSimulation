class Grid:
    def __init__(self, gridConsumption=0):
        self.gridConsumption = gridConsumption
    
    def getGridConsumption(self):
        return self.gridConsumption
    
    def setGridConsumption(self, newGridConsumption):
        self.gridConsumption = newGridConsumption