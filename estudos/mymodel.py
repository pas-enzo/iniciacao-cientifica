import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = 'C:\\Users\\Windows 10\\Documents\\IC\\Code\\data\\melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne dataS
print(melbourne_data.describe())