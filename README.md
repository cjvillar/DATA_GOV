# [data.gov](https://catalog.data.gov/dataset/)

Various interesting datasets from data.gov that I'd like to explore.

## Tools:
[chartsjs](https://www.chartjs.org/)

## Notes on scripts

Quick check a CSVs data:
```Bash
cat data/SharkIncidents_1950_2022_220302\ -\ Attacks_1950_2021.csv| awk '/White/ && /Surfing/' | wc -l
```
Truncate a big dataset (csv):
```Bash
./scripts/copy_rows.sh data/Police_Department_Incident_Reports__2018_to_Present.csv data/PD_Incident_Reports_2018_to_Present_100_rows.csv 100
```
