# Import libraries
import pandas as pd
import random


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
    a = map(lambda x: x.lower(), values)
    data = data[data[category].isin(a)]
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
    global data
    data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')

# assign dataset 
pd.options.display.max_rows = 9999
# df = df.dropna()
data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
Reset_data()


# Retrieve a link of a product
def Read_Input(Dictionary):
  IDs = Filter(Dictionary)
  link = []
  for id in IDs:
    # print(Find_Row_ID(id))
    link.extend(Find_Cell_ID(id,"Link"))
  return Randomize_Value(link)
def Randomize_Value(list):
  return random.choice(list)

# Search by value
def Search_By_Value(value):
  delta = value/100
  return Filter_Values("Price", value - delta , value + delta)

# Collect input from user and turn it into a dictionary
def Get_Input(input):
  keywords = Get_Keywords(input)
  categories = Get_Categories(keywords)
  dict = Get_Dict(categories, keywords)
  print(dict)
  return Filter(dict)

def Get_Keywords(input):
  # Turn a sentence into a list of words
  keywords = set(input.split())
  # Delete special characters
  # FIlter useful keywords
  # print(keywords)
  return keywords

def Get_Categories(keywords):
  # Find categories of keywords
  categories = set(Check_Keyword(keywords))
  # print(categories)
  return categories

def Get_Dict(keys, values):
  global Template
  # Create a dictionary and keys with no values
  dictionary = {}
  # Add values to dictionary
  for key in keys:
    list = []
    temp = values
    for value in temp:
      # if value in Template[key]:
      list.append(value)
      # values.remove(value)
    dictionary[key] = list
  return dictionary

def Check_Keyword(value):
  global Template
  return value

Get_Input(input("Enter some text: ").lower())






# Data template for testing purposes


# Template = {
#   "name": ["PLATSA","VIMLE","TROFAST"],
#   "id": [80308699,19302328,89305446,79248588]
# }
# Filter(Template)


# Testing functions
# Don't run this file 


# # # Filtering
# values = ["PLATSA","VIMLE","TROFAST"]
# Filter_Func("Name", values)
# Sort_Func("Name")
# print(Filter_Func("Name", values))
# print("----------------------------------------------------------------")

# # Print a column
# Sort_Func("ID")
# print(data["ID"])
# print("----------------------------------------------------------------")
# # Print a row
# print(data.loc[data.index[3]])
# print("----------------------------------------------------------------")
# # Print a cell
# print(data["Description"].loc[data.index[0]])
# print("----------------------------------------------------------------")