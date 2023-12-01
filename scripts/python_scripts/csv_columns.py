import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Read a CSV file into a pandas DataFrame')
    parser.add_argument('file_path', metavar='file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    #CSV to a pd 
    file_path = args.file_path
    data_frame = pd.read_csv(file_path)

    #columns
    print("Columns:")
    print(data_frame.columns.tolist())

    #number of rows in each column
    print("\nNumber of rows in each column:")
    print(data_frame.count())

if __name__ == "__main__":
    main()
