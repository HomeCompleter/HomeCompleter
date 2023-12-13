# Import libraries
import pandas as pd
from _finding import *
import random


# Run to get data from the raw_data file and analyse user's input
# 
# 


# Read raw data
df = pd.read_csv("Project\dataset\Raw_Data.csv", encoding='cp1252')
# df = df.dropna()

# Write data
with open("Project\dataset\Dataset.csv", 'w', newline='') as f:
    f.write(df.to_csv(index=True))
Reset_data()

# # Print list of categories
# category_list = pd.read_csv("Project\dataset\Dataset.csv", encoding='cp1252', index_col=0, nrows=0).columns.tolist()
# print(category_list)

# Dictionary test

def Read_Input(Dictionary):
  IDs = Filter(Dictionary)
  link = []
  for id in IDs:
    # print(Find_Row_ID(id))
    link.extend(Find_Cell_ID(id,"Link"))
  return link

def Randomize_Value(list):
  return random.choice(list)

def Search_By_Value(value):
  delta = value/100
  return Filter_Values("Price", value - delta , value + delta)

def Create_Dictionary():
  dict = {}
  return

# Reset_data(data)
prompt = {
  "Name": ["PLATSA","VIMLE","TROFAST"],
  "ID": [80308699,19302328,89305446,79248588]
}

link = Read_Input(prompt)
print(link)