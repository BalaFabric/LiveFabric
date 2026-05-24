# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7e8e6dfe-8f95-4910-a5a4-40079bfc8fa1",
# META       "default_lakehouse_name": "TestLH",
# META       "default_lakehouse_workspace_id": "3795deb5-7001-4008-8799-70424fc3aa0a",
# META       "known_lakehouses": [
# META         {
# META           "id": "7e8e6dfe-8f95-4910-a5a4-40079bfc8fa1"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DimDate (DateKey, FullDate, Year, Month, MonthName, Quarter)
# MAGIC VALUES
# MAGIC (20240510, '2024-05-10', 2024, 5, 'May', 2),
# MAGIC (20240511, '2024-05-11', 2024, 5, 'May', 2),
# MAGIC (20240512, '2024-05-12', 2024, 5, 'May', 2);

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM DimDate

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
