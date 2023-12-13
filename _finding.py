# Import Libraries
import pandas as pd


# This script is used to find datas from given dataset using datas and their categories collected
# from user's input. Including sorting function, filtering function, and finding datas using ID


# Find by ID function
def Create_ID_List():
    global data
    IDs = data["ID"].tolist()
    Reset_data()
    return IDs
def Find_Row_ID(value):
    global csvData
    data = csvData[csvData["ID"]==value]
    return data
def Find_Cell_ID(value, category):
    global csvData
    data = csvData[csvData["ID"]==value][category].tolist()
    return data

# Sort Function
def Sort_Func(category):
    global data
    data.sort_values([category],
                    axis=0, 
                    ascending=[True],  
                    inplace=True)
    
# Filter Function (multi-valued)
def Filter_Func(category, values):
    global data
    data = data[data[category].isin(values)]
    return Create_ID_List()
def Filter_Values(category, left, right):
    global data
    data = data[data['category'] >= left and data['category'] <= right]
    return Create_ID_List()
def Filter(input):
    for category in input.keys():
        Filter_Func(category, input[category])
    return Create_ID_List()

# Reset data
def Reset_data():
    global csvData
    global data
    data = csvData

# assign dataset 
pd.options.display.max_rows = 9999
csvData = pd.read_csv("Project\dataset\Dataset.csv", encoding='cp1252')
# df = df.dropna()
data = csvData
Reset_data()

# Testing functions
# Don't run this file 


# Filtering
values = ["PLATSA","VIMLE","TROFAST"]
Filter_Func("Name", values)
Sort_Func("Name")
print(data)
print("----------------------------------------------------------------")

# Print a column
Sort_Func("ID")
print(data["ID"])
print("----------------------------------------------------------------")
# Print a row
print(data.loc[data.index[3]])
print("----------------------------------------------------------------")
# Print a cell
print(data["Description"].loc[data.index[0]])
print("----------------------------------------------------------------")