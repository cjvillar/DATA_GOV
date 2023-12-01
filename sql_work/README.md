## SQL Work

Create a db from data, if .csv use:
python scripts/python_scripts/csv_to_sql_db.py

have fun with querries.

## Get Started:
Open db
```Bash
sqlite3 PD_Incident_Reports_2018_to_Present_100_rows.db
```
```Bash
sqlite> .schema
```
```Bash
sqlite> .exit
```

### Samples

This is similar to the python pivot table script


```Sql
SELECT "Incident Day of Week", "Incident Category", COUNT(*) AS "Number of Incidents"
FROM table_name -- Yea, forgot to change edit the table name
GROUP BY "Incident Day of Week", "Incident Category"
ORDER BY "Incident Day of Week", "Number of Incidents" DESC;

```

