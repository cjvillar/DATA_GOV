'''
Use this script to create an SQLite db
from data in a .csv. 

TODO: add argparse pos arguments so that users do not have to 
change the script code directly 

'''

import sqlite3
import pandas as pd


csv_file = 'data/SharkIncidents_1950_2022_220302 - Attacks_1950_2021.csv'

# read in CSV data into DataFrame
data = pd.read_csv(csv_file)

# SQLite database to be made
db_file = 'SharkIncidents_1950_2022.db'  # db name

# connect to the SQLite db (creates the database if it doesn't exist)
conn = sqlite3.connect(db_file)

# save df to SQLite db table. change 'table_name' to desired table name
data.to_sql('incidents', conn, if_exists='replace', index=False)  

# commit changes and close the connection
conn.commit()
conn.close()

print(f"SQLite database '{db_file}' created successfully.")
