# Import libraries
import pandas as pd
import random
import json
import torch
from nltk_utils import tokenize,stem


# This script is used to find datas from given dataset using datas and their categories collected
# from user's input. Including sorting function, filtering function, and finding datas using ID


# Find by ID function
def Create_ID_List():
    global data
    ids = []
    ids = data["id"].tolist()
    return ids
def Find_Row_ID(value):
    global data
    data = data[data["id"]==value]
    return data
def Find_Cell_ID(value, category):
    global data
    list = data[data["id"]==value][category].tolist()
    return list

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
    # print(category,values)

    data = data[data[category].isin([stem(word) for word in values])  ]
    print(data[category])
    return Create_ID_List()
def Filter_Values(category, left, right):
    global data
    data = data[data[category] >= left and data[category] <= right]
    return Create_ID_List()
def Filter(input):
    for category in input.keys():
        Filter_Func(category, input[category])
    return Create_ID_List()

# Reset data
def Reset_data():
    global data
    data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
    print("Let's chat! (type 'quit' to exit) (type 'reset' to reset)")

# Retrieve a link of a product
def Read_Input(IDs):
  link = []
  for id in IDs:
    # print(Find_Row_ID(id))
    link.extend(Find_Cell_ID(id,"link"))
  return Randomize_Value(link)
def Randomize_Value(list):
  if not list: return "No value"
  return random.choice(list)

# Search by value
def Search_By_Value(value):
  delta = value/100
  return Filter_Values("Price", value - delta , value + delta)

# Collect input from user and turn it into a dictionary
def Get_Input(input):
  keywords = Get_Keywords(input.lower())
  categories = Get_Categories(keywords)
  dict = Get_Dict(categories, keywords)
  # print("Dict:", dict)
  return Filter(dict)

def Get_Keywords(input):
  # Turn a sentence into a list of words
  list = []
  keywords = tokenize(input)
  keywords = set([stem(w) for w in keywords])
  for keyword in keywords:
     if keyword in all_words:
        list.append(keyword)
  # Delete special characters
  # FIlter useful keywords
  # print("keyword:", list)
  return list

def Get_Categories(keywords):
  # Find categories of keywords
  categories = set(Check_Keyword(keywords))
  # print("categories:", categories)
  return categories

def Get_Dict(keys, values):
  global Template
  # Create a dictionary and keys with no values
  dictionary = {}
  # Add values to dictionary
  for key in keys:
    list = []
    for intent in intents['intents']:
      if intent['tag'] == key:
        for item in intent['patterns']:
          for value in values:
            if value in [stem(word) for word in tokenize(item.lower())]:
              list.append(value)
              # values.remove(value)
        # print(list)
        dictionary[key] = list
      # print(dictionary)
  return dictionary

def Check_Keyword(values):
  list = []
  for value in values:
     for intent in intents['intents']:
        for item in intent['patterns']:
          if value in [stem(word) for word in tokenize(item.lower())]:
            list.append(intent['tag'])
  # print("Tags",list)
  return list

# assign dataset 
pd.options.display.max_rows = 9999
data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
Reset_data()

with open('tags.json', 'r') as json_data:
  intents = json.load(json_data)
  store = intents['intents']

FILE = "tags.pth"
df = torch.load(FILE)

input_size = df["input_size"]
hidden_size = df["hidden_size"]
output_size = df["output_size"]
all_words = df['all_words']
tags = df['tags']
model_state = df["model_state"]

# print(all_words, tags)

# if __name__ == "__main__":
#     while True:
#         # sentence = "do you use credit cards?"
#         sentence = input("You: ")
#         if sentence == "quit":
#           break
#         if sentence == "reset":
#           Reset_data()
#           continue
#         list = Get_Input(sentence)
#         print(Read_Input(list))



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