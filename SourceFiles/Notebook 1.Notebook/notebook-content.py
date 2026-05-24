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
# MAGIC  CREATE TABLE DimDate (
# MAGIC     DateKey INT  ,
# MAGIC     FullDate DATE,
# MAGIC     Year INT,
# MAGIC     Month INT,
# MAGIC     MonthName VARCHAR(20),
# MAGIC     Quarter INT
# MAGIC );


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DimDate (DateKey, FullDate, Year, Month, MonthName, Quarter)
# MAGIC VALUES
# MAGIC (20260526, '2026-05-30', 2026, 5, 'May', 2)

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DimDate (DateKey, FullDate, Year, Month, MonthName, Quarter)
# MAGIC VALUES
# MAGIC (20240101, '2024-01-01', 2024, 1, 'January', 1),
# MAGIC (20240102, '2024-01-02', 2024, 1, 'January', 1),
# MAGIC (20240215, '2024-02-15', 2024, 2, 'February', 1),
# MAGIC (20240310, '2024-03-10', 2024, 3, 'March', 1),
# MAGIC (20240405, '2024-04-05', 2024, 4, 'April', 2);

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT *  FROM DimDate

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DimDate (DateKey, FullDate, Year, Month, MonthName, Quarter)
# MAGIC VALUES
# MAGIC (20240101, '2024-01-01', 2024, 1, 'January', 1),
# MAGIC (20240102, '2024-01-02', 2024, 1, 'January', 1),
# MAGIC (20240215, '2024-02-15', 2024, 2, 'February', 1),
# MAGIC (20240310, '2024-03-10', 2024, 3, 'March', 1),
# MAGIC (20240405, '2024-04-05', 2024, 4, 'April', 2),
# MAGIC (20260522, '2026-05-22', 2026, 5, 'May', 2),
# MAGIC (20260523, '2026-05-23', 2026, 5, 'May', 2),
# MAGIC (20260525, '2026-05-25', 2026, 5, 'May', 2),
# MAGIC (20260524, '2026-05-24', 2026, 5, 'May', 2),
# MAGIC (20260526, '2026-05-26', 2026, 5, 'May', 2),
# MAGIC (20260527, '2026-05-27', 2026, 5, 'May', 2),
# MAGIC (20260528, '2026-05-28', 2026, 5, 'May', 2),
# MAGIC (20260528, '2026-05-29', 2026, 5, 'May', 2),
# MAGIC (20260526, '2026-05-30', 2026, 5, 'May', 2),
# MAGIC (20260526, '2026-06-01', 2026, 6, 'June', 2),
# MAGIC (20260526, '2026-06-02', 2026, 6, 'June', 2),
# MAGIC (20260526, '2026-06-03', 2026, 6, 'June', 2);

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DimProduct
# MAGIC (
# MAGIC     ProductKey,
# MAGIC     ProductID,
# MAGIC     ProductName,
# MAGIC     Category
# MAGIC )
# MAGIC VALUES
# MAGIC (
# MAGIC     CAST(-1 AS BIGINT),
# MAGIC     NULL,
# MAGIC     'Unknown',
# MAGIC     'Unknown'
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM factsales
# MAGIC ORDER BY SalesKey

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
