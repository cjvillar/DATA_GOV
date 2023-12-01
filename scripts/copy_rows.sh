#!/bin/bash

#usage: copy_rows.sh <input_file.csv> <output_file.csv> <number_of_rows: int>

#check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_file.csv> <output_file.csv> <number_of_rows>"
    exit 1
fi

input_file="$1"
output_file="$2"
num_rows="$3"

# input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file not found!"
    exit 1
fi

# copy given number of rows to the output file
head -n "$num_rows" "$input_file" > "$output_file"

echo "Copied $num_rows rows from $input_file to $output_file"