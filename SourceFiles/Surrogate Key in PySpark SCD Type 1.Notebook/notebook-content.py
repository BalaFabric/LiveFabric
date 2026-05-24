# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2d91e8b0-0248-4cac-af3f-a2ab4b25d3e5",
# META       "default_lakehouse_name": "DemoLH",
# META       "default_lakehouse_workspace_id": "3795deb5-7001-4008-8799-70424fc3aa0a",
# META       "known_lakehouses": [
# META         {
# META           "id": "2d91e8b0-0248-4cac-af3f-a2ab4b25d3e5"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS StagingCustomer
# MAGIC (
# MAGIC     CustomerId INT,
# MAGIC     CustomerName VARCHAR(100),
# MAGIC     CustomerGender VARCHAR(100),
# MAGIC     CusstomerLocation VARCHAR(100),
# MAGIC     CustomerCountry VARCHAR(100)
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM StagingCustomer

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS DimCustomer
# MAGIC (
# MAGIC     CustomerKey INT,
# MAGIC     CustomerId INT,
# MAGIC     CustomerName VARCHAR(100),
# MAGIC     CustomerGender VARCHAR(100),
# MAGIC     CusstomerLocation VARCHAR(100),
# MAGIC     CustomerCountry VARCHAR(100)
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

staging_df = spark.table("StagingCustomer")
dim_df = spark.table("DimCustomer")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

new_records = staging_df.join(
    dim_df,
    "CustomerId",
    "left_anti"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import max

max_key = dim_df.agg(max("CustomerKey")).collect()[0][0]

if max_key is None:
    max_key = 0

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

window_spec = Window.orderBy("CustomerId")

new_records_with_sk = new_records.withColumn(
    "CustomerKey",
    row_number().over(window_spec) + max_key
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

new_records_with_sk.createOrReplaceTempView("NewCustomers")
staging_df.createOrReplaceTempView("StagingCustomers")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC MERGE INTO DimCustomer AS target
# MAGIC USING (
# MAGIC     SELECT
# MAGIC         n.CustomerKey,
# MAGIC         s.CustomerId,
# MAGIC         s.CustomerName,
# MAGIC         s.CustomerGender,
# MAGIC         s.CusstomerLocation,
# MAGIC         s.CustomerCountry
# MAGIC     FROM StagingCustomers s
# MAGIC     LEFT JOIN NewCustomers n
# MAGIC     ON s.CustomerId = n.CustomerId
# MAGIC ) source
# MAGIC ON target.CustomerId = source.CustomerId
# MAGIC 
# MAGIC WHEN MATCHED AND (
# MAGIC     target.CustomerName <> source.CustomerName OR
# MAGIC     target.CustomerGender <> source.CustomerGender OR
# MAGIC     target.CusstomerLocation <> source.CusstomerLocation OR
# MAGIC     target.CustomerCountry <> source.CustomerCountry
# MAGIC )
# MAGIC THEN UPDATE SET
# MAGIC     target.CustomerName = source.CustomerName,
# MAGIC     target.CustomerGender = source.CustomerGender,
# MAGIC     target.CusstomerLocation = source.CusstomerLocation,
# MAGIC     target.CustomerCountry = source.CustomerCountry
# MAGIC 
# MAGIC WHEN NOT MATCHED
# MAGIC THEN INSERT (
# MAGIC     CustomerKey,
# MAGIC     CustomerId,
# MAGIC     CustomerName,
# MAGIC     CustomerGender,
# MAGIC     CusstomerLocation,
# MAGIC     CustomerCountry
# MAGIC )
# MAGIC VALUES (
# MAGIC     source.CustomerKey,
# MAGIC     source.CustomerId,
# MAGIC     source.CustomerName,
# MAGIC     source.CustomerGender,
# MAGIC     source.CusstomerLocation,
# MAGIC     source.CustomerCountry
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM DimCustomer
# MAGIC ORDER BY CustomerKey 

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
