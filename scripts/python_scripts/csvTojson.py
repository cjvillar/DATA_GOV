"""
Convert a .csv to json with python.

usage: python csvTojson.py in.csv out.json

"""

import csv
import json
import argparse

def to_json(csvFilePath, jsonFilePath):
   
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        header = csvReader.fieldnames #returns header
    
        if header:
            data = [{key: row[key] for key in header} for row in csvReader]
        
   

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('csvFilePath', type=str, help='Path to the input CSV file')
    parser.add_argument('jsonFilePath', type=str, help='Path to the output JSON file')

    args = parser.parse_args()

    to_json(args.csvFilePath, args.jsonFilePath)
