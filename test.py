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
	# Filter_Values("price", min(list_of_numbers), max(list_of_numbers))
	return [data["id"].tolist()]
def Find_Row_ID(value):
	global data
	data = data[data["id"]==value]
	return data
def Find_Cell_ID(value, category):
	global data
	return str(data[data["id"]==value][category])
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
	return Create_ID_List()

# Search by value
def Search_By_Value(value):
	return Filter_Values("price", value*0.9 , value*1.1)

def Randomize_Value(IDs):
	if not IDs: return "I'm apologies for this inconvenient. We found 0 result based on your requirement. Please type 'reset' to reset the procedure."
	rand = random.choice(IDs)
	response = Find_Cell_ID(rand,"name"), "/", Find_Cell_ID(rand,"link")
	# print(IDs,rand)
	return 1
# ------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------
# Reset data
def Reset_data():
	global data
	data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
	print("Let's chat! (type 'quit' to exit) (type 'reset' to reset)")
	global list_of_numbers
	list_of_numbers = [0,3000]
	return

# Retrieve a link of a product
def Read_Input(IDs):
	return "Found a product: ", Randomize_Value(IDs)

# ------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------

# Collect input from user and turn it into a dictionary
def Get_Input(input):
	keywords = Get_Keywords(input)
	categories = Get_Categories(keywords)
	dict = Get_Dict(categories, keywords)
	print("Dict:", dict)
	if bool(dict): return Filter(dict)
	else: return "Can't find what you're looking for. Maybe you should mention more about it?"

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
					print("Tags",list)
	return list

def Get_Dict(keys, values):
	# Create a dictionary and keys with no values
	dictionary = {}
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
	print(dictionary)
	return dictionary
# ------------------------------------------------------------------------------------------------

# assign dataset 
pd.options.display.max_rows = 9999
data = pd.read_csv("dataset\Dataset.csv", encoding='cp1252')
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


list_of_numbers = [0,3000]
# print(all_words, tags)
# print(data)

if __name__ == "__main__":
	while True:
		# sentence = "do you use credit cards?"
		sentence = input("You: ")
		if sentence == "quit":
			break
		if sentence == "reset":
			Reset_data()
			continue
		list = Get_Input(sentence)
		print(Read_Input(list))