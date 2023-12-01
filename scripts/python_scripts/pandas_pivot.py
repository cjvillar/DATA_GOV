import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'data/PD_Incident_Reports_2018_to_Present_100_rows.csv'
#read in csv to dataframe
df = pd.read_csv(file_path)

#check column names
column_names = [col for col in df.columns]
#print(column_names)

# Creating a pivot table using pandas
pivot_table = pd.pivot_table(df, 
                             values='Incident Subcategory', 
                             index='Incident Day of Week', 
                             columns='Incident Category', 
                             aggfunc=np.size,
                             fill_value=0)


# plot the pivot table  as bar chart
pivot_table.plot.barh(figsize=(12,8),
                      title='Number Of Incidents By Category Based On Day Of The Week')
plt.xlabel('Number of Incidents')
plt.ylabel('Day of the Week')
plt.legend(title='Incident Category')
plt.show()