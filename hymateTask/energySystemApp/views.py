from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .components.battery import Battery
from .components.cleanEnergy import CleanEnergy
from .components.grid import Grid
from .components.household import Household
from .energyManagement.energyManagement import EnergyManager
from .src.load_data import CSVProcessor
from django.views.decorators.csrf import csrf_protect
import pandas as pd


@csrf_protect
def index(request):

    if request.method == 'POST':
        producer_count = request.POST.get('producer_count')
        battery_count = request.POST.get('battery_count')
        max_battery_capacity = request.POST.get('max_battery_capacity')
        
        #Initialize components
        grid = Grid(gridConsumption=0)
        household = Household(neededConsumption=0)
        energyManager = EnergyManager(producingEnergiesNumber=int(producer_count), 
                                        batteryStockageNumber=int(battery_count), 
                                        maxBatteryCapacity=int(max_battery_capacity)*1000, 
                                        grid=grid,
                                        household=household,
                                        time=0)


        myDataProcessor = CSVProcessor(inputCSVpath="energySystemApp/data/profiles_dataset.csv", 
                                        outputCSVpath="energySystemApp/data/simulatedData.csv")
        
        profileData = myDataProcessor.load_data()

        timestampData = []
        cleanEnergyLeftData = []
        batteryEnergyAvailableData = []
        gridConsumptionData = []

        for index, row in profileData.iterrows():
            cleanEnergyValue, householdConsumption, timestamp = myDataProcessor.retrieveDataFromRow(row)
            energyManager.updateCleanEnergy(cleanEnergyValue)
            energyManager.updateHouseholdNeeds(householdConsumption)
            energyManager.giveEnergy()
            cleanEnergyLeft, batteryEnergyAvailable, gridConsumption = energyManager.retrieveValuesFromComponents()
            timestampData.append(timestamp)
            cleanEnergyLeftData.append(cleanEnergyLeft)
            batteryEnergyAvailableData.append(batteryEnergyAvailable)
            gridConsumptionData.append(gridConsumption)

        columnNames = ['timestamp', 'clean_energy_left', 'battery_energy_available', 'grid_consumption']
        columnValues = [timestampData, cleanEnergyLeftData, batteryEnergyAvailableData, gridConsumptionData]
        resultCSV = pd.DataFrame(list(map(list, zip(*columnValues))), columns=columnNames)
        myDataProcessor.saveData(resultCSV)

        context = {'currenturl': 'index',
                    'simulation': "Simulation Finished. You will find the simulatedData.csv file in the folder data, "}

        return render(request, 'index.html', context)

    return render(request, 'index.html')
