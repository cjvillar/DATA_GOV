#!/bin/bash

#usage: ./analyze_data.sh <.csv> or <.tsv>

#check for filename is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide the filename as an argument."
  exit 1
fi

filename=$1

#check file exists
if [ ! -f "$filename" ]; then
  echo "File not found."
  exit 1
fi

echo "Column Names:"
#print the column names
head -n 1 "$filename" | tr ',' '\n' | awk '{$1=$1};1'

echo "Number of Rows:"
#count rows excluding the header
num_rows=$(awk 'NR>1 {count++} END {print count}' "$filename")
echo "$num_rows"

echo "Top Value in Each Column:"
#print the top value in each column, slow for big datasets TODO: make faster
awk -F',' 'NR>1 {for (i=1; i<=NF; i++) {if (a[i]==""){a[i]=$i}}} END {for (i=1; i<=NF; i++) {print "Column " i ": " a[i]}}' "$filename"
