import pandas
import csv

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (key,row) in data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter any word: ").upper() # N I S H A N T
result_list = [new_dict[key] for key in user_input]
print(result_list)
