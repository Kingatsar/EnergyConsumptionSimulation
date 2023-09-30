import pandas as pd

class CSVProcessor:
    def __init__(self, inputCSVpath, outputCSVpath):
        self.inputCSVpath = inputCSVpath
        self.outputCSVpath = outputCSVpath

    def load_data(self):
        # Load the CSV into a DataFrame
        self.df = pd.read_csv(self.inputCSVpath)
        return self.df

    def createNewDataframe(self):
        return pd.DataFrame(columns=self.df.columns)

    def retrieveDataFromRow(self,row):
        timestamp = row['timestamp']
        cleanEnergyValue = row['pv_yield_power']
        householdConsumption = row['household_consumption']
        return cleanEnergyValue, householdConsumption, timestamp
    
    def addDataRowToDataframe(self, row, dataframe):
        dataframe = dataframe.append(row, ignore_index=True)
        return dataframe    

    def saveData(self, myDataframe):
        # Save the updated DataFrame to a new CSV file
        myDataframe.to_csv(self.outputCSVpath, index=False)

