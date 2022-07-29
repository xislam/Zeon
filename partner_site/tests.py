import csv

import pandas as pd


# Extract data from Excel spreadsheet
read_file = pd.read_excel(r"web_to_spreadsheet.xls")

# Convert data to CSV formatted file
read_file.to_csv(r"kg_cities.csv", index=True, header=True)
