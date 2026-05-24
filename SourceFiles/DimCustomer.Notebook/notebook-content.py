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

df = spark.read.csv(path='abfss://TestClass@onelake.dfs.fabric.microsoft.com/TestLH.Lakehouse/Files/Development/Customer.csv',header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('StagingCustomer')

# METADATA ********************

# META {
# META   "language": "python",
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
# MAGIC     CustomerID INT,
# MAGIC     CustomerName VARCHAR(100),
# MAGIC     City VARCHAR(100),
# MAGIC     Country VARCHAR(100)
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
    "CustomerID",
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

window_spec = Window.orderBy("CustomerID")

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
# MAGIC         s.CustomerID,
# MAGIC         s.CustomerName,
# MAGIC         s.City,
# MAGIC         s.Country
# MAGIC     FROM StagingCustomers s
# MAGIC     LEFT JOIN NewCustomers n
# MAGIC     ON s.CustomerID = n.CustomerID
# MAGIC ) source
# MAGIC ON target.CustomerID = source.CustomerID
# MAGIC 
# MAGIC WHEN MATCHED AND (
# MAGIC     target.CustomerName <> source.CustomerName OR
# MAGIC     target.City <> source.City OR
# MAGIC     target.Country <> source.Country 
# MAGIC )
# MAGIC THEN UPDATE SET
# MAGIC     target.CustomerName = source.CustomerName,
# MAGIC     target.City = source.City,
# MAGIC     target.Country = source.Country
# MAGIC 
# MAGIC WHEN NOT MATCHED
# MAGIC THEN INSERT (
# MAGIC     CustomerKey,
# MAGIC     CustomerID,
# MAGIC     CustomerName,
# MAGIC     City,
# MAGIC     Country
# MAGIC )
# MAGIC VALUES (
# MAGIC     source.CustomerKey,
# MAGIC     source.CustomerID,
# MAGIC     source.CustomerName,
# MAGIC     source.City,
# MAGIC     source.Country
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
