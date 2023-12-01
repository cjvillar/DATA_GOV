import csv
import matplotlib.pyplot as plt



def pie_chart(csvFilePath):
    list_of_dicts = []
    with open(csvFilePath, 'r', encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            list_of_dicts.append(row)

    species = {}
    #create a new dict of species and how many per dict in list of dict
    for entry in list_of_dicts:
        species_name = entry["Species"]
        species[species_name] = species.get(species_name, 0) + 1

 

    # Create a pie chart
    labels = species.keys()
    values = species.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  #equal aspect ratio for circular pie chart.

    # Set the title
    plt.title(f'Pie Chart')

    #show chart
    plt.show()

#usage:
csvFilePath = 'data/SharkIncidents_1950_2022_220302 - Attacks_1950_2021.csv'  

pie_chart(csvFilePath)
