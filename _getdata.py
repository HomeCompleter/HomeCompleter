# Import libraries
import pandas as pd
import csv
from nltk_utils import tokenize,stem

# Read raw data
df = pd.read_csv("dataset\Raw_Data.csv", encoding='cp1252')
# for row in df["price"]:
#     if type(row) == str:
#         row = row.replace('SR', '')
#         row = row.replace(',', '')
#         row = float(row)
#     row = row
# df["price"] = df["price"].replace(',', '')

# df['price'] = df['Status'].replace({'P': 'A'}) 
# df.loc[(df.Name.isin(['Avi','Dav','Ron'])) & (df.Age < 33), 'Babys'] += 1
# df.loc[(),"price"] = df.loc[(),"price"].replace(',', '')

# Write data
with open("dataset\Dataset.csv", 'w', newline='') as f:
    f.write(df.to_csv())
# with open("dataset\Dataset.csv", 'w', newline='') as f:
#     f["price"] = df["price"].replace([',','SR'], '')
#     f.write(df.to_csv())
#     print(df["price"])

# Open the CSV file
with open('dataset\Dataset.csv', 'r') as file:
    # Read the CSV file
    reader = csv.reader(file)
    # Create a new list to store the lowercase data
    lowercase_data = []
    # Loop through each row in the CSV file
    for row in reader:
        # Create a new list to store the lowercase row data
        lowercase_row = []
        # Loop through each column in the row
        for column in row:
            # Convert the column to lowercase and append it to the lowercase row list
            column = stem(column)
            lowercase_row.append(column.lower())
            
        # Append the lowercase row list to the lowercase data list
        lowercase_data.append(lowercase_row)

# Open a new file to write the lowercase data
with open('dataset\Dataset.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the lowercase data to the new CSV file
    writer.writerows(lowercase_data)

# Run to get data from the raw_data file and analyse user's input
# 
# 

# # Print list of categories
# category_list = pd.read_csv("dataset\Dataset.csv", encoding='cp1252', index_col=0, nrows=0).columns.tolist()
# print(category_list)

