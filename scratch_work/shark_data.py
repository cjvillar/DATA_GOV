import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'data/SharkIncidents_1950_2022_220302 - Attacks_1950_2021.csv'


df = pd.read_csv(file_path)

column_names =  [col for col in df.columns]

#filter only White sharks
filtered_df = df[df['Species'] == 'White']

pivot_table = pd.pivot_table(filtered_df,
                             index='Species',
                             columns='County',
                             aggfunc=np.size,
                             fill_value=0)


print(pivot_table.columns)

# selected_county = 'Marin'
# data_for_pie = pivot_table[selected_county]

# # Plotting a pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(data_for_pie, labels=data_for_pie.index, autopct='%1.1f%%', startangle=140)
# plt.title(f'Number Of White Shark Attacks in County {selected_county}')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()