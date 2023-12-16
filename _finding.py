# Import libraries
import pandas as pd
import random
import json
import torch
from nltk_utils import tokenize,stem


# This script is used to find datas from given dataset using datas and their categories collected
# from user's input. Including sorting function, filtering function, and finding datas using ID


# ------------------------------------------------------------------------------------------------
# Find by ID function
def Create_ID_List():
	global data
	Filter_Values("price", min(list_of_numbers), max(list_of_numbers))
	print(list_of_numbers)
	return Read_Input([data["id"].tolist()])
def Find_Row_ID(value):
	global data
	data = data[data["id"]==value]
	return
def Find_Cell_ID(value, category):
	global data
	return data[data["id"]==value][category].tolist()
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# Sort Function
def Sort_Func(category):
	global data
	data.sort_values([category],axis=0, ascending=[True],inplace=True)
	return
    
# Filter Function (multi-valued)
def Filter_Func(category, values):
	global data
	data = data[data[category].isin([stem(word) for word in values])]
	# print(data[category])
	return

def Filter_Values(category, left, right):
	global data
	data = data[data[category] <= right]
	data = data[data[category] >= left]
	return

def Filter(input):
	for category in input.keys():
		Filter_Func(category, input[category])
	# print(data)
	return Create_ID_List()

# Search by value
def Search_By_Value(value):
	return Filter_Values("price", value*0.9 , value*1.1)
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# Reset data
def Reset_data():
	global data
	global list_of_numbers
	data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
	print("Let's chat! (type 'quit' to exit) (type 'reset' to reset)")
	list_of_numbers = [0,3000]
	return "Data renewed successfully. Ready for the next input."

# Retrieve a link of a product
def Read_Input(IDs):
	link = []
	for id in IDs:
		# print(Find_Row_ID(id))
		link.extend(Find_Cell_ID(id,"link"))
	return Randomize_Value(link)

def Randomize_Value(list):
	if not list: return "No products found. Please type 'reset' to reset the procedure."
	return ("Found a product: ", random.choice(list))
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Collect input from user and turn it into a dictionary
def Get_Input(input): 
	if input=="reset": return Reset_data()
	keywords = Get_Keywords(input)
	categories = Get_Categories(keywords)
	dict = Get_Dict(categories, keywords)
	print("Dict:", dict)
	if len(dict) == 0: return ("Can't find what you're looking for. Maybe you should mention more about it?")
	else: return Filter(dict) 

def Get_Keywords(input):
	# Turn a sentence into a list of words
	global list_of_numbers
	list = []
	keywords = tokenize(input)
	keywords = set([stem(w) for w in keywords])
	for keyword in keywords:
		if keyword in all_words:
			list.append(keyword)
		elif keyword.isdigit():
			list_of_numbers.append(float(keyword))
	print("keyword:", list)
	return list

def Get_Categories(keywords):
	# Find categories of keywords
	categories = set(Check_Keyword(keywords))
	print("categories:", categories)
	return categories

def Check_Keyword(values):
	list = []
	for value in values:
		for intent in intents['intents']:
			for item in intent['patterns']:
				if value in [stem(word) for word in tokenize(item.lower())]:
					list.append(intent['tag'])
		# print("Tags",list)
	return set(list)

def Get_Dict(keys, values):
	# Create a dictionary and keys with no values
	dictionary = {}
	for key in keys:
		list = []
		for intent in intents['intents']:
			if intent['tag'] == key:
				for value in values:
					for item in intent['patterns']:
						if value in [stem(word) for word in tokenize(item.lower())]:
							list.append(value)
							break
							# values.remove(value)
							# print(list)
				dictionary[key] = list
	# print(dictionary)
	return dictionary
# ------------------------------------------------------------------------------------------------

# assign dataset 
pd.options.display.max_rows = 9999
data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
list_of_numbers = []
Reset_data()

with open("tags.json", 'r') as json_data:
	intents = json.load(json_data)

FILE = "tags.pth"
df = torch.load(FILE)

input_size = df["input_size"]
hidden_size = df["hidden_size"]
output_size = df["output_size"]
all_words = df['all_words']
tags = df['tags']
model_state = df["model_state"]

# Search_By_Value(10)
# Filter_Values("price", 0, 1)
# print(data)
# print(all_words, tags)

if __name__ == "__main__":
	while True:
		# sentence = "do you use credit cards?"
		sentence = input("You: ")
		if sentence == "quit":
			break
		if sentence == "reset":
			Reset_data()
			continue
		print(Get_Input(sentence))