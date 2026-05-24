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

df = spark.read.csv(path='abfss://TestClass@onelake.dfs.fabric.microsoft.com/TestLH.Lakehouse/Files/Development/Product.csv',header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('StagingProduct')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM StagingProduct

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS DimProduct
# MAGIC (
# MAGIC     ProductKey INT,
# MAGIC     ProductID INT,
# MAGIC     ProductName VARCHAR(100),
# MAGIC     Category VARCHAR(100)
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

staging_df = spark.table("StagingProduct")
dim_df = spark.table("DimProduct")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

new_records = staging_df.join(
    dim_df,
    "ProductID",
    "left_anti"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import max

max_key = dim_df.agg(max("ProductKey")).collect()[0][0]

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

window_spec = Window.orderBy("ProductID")

new_records_with_sk = new_records.withColumn(
    "ProductKey",
    row_number().over(window_spec) + max_key
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

new_records_with_sk.createOrReplaceTempView("NewProducts")
staging_df.createOrReplaceTempView("StagingProduct")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC MERGE INTO DimProduct AS target
# MAGIC USING (
# MAGIC     SELECT
# MAGIC         n.ProductKey,
# MAGIC         s.ProductID,
# MAGIC         s.ProductName,
# MAGIC         s.Category
# MAGIC     FROM StagingProduct s
# MAGIC     LEFT JOIN NewProducts n
# MAGIC     ON s.ProductID = n.ProductID
# MAGIC ) source
# MAGIC ON target.ProductID = source.ProductID
# MAGIC 
# MAGIC WHEN MATCHED AND (
# MAGIC     target.ProductName <> source.ProductName OR
# MAGIC     target.Category <> source.Category
# MAGIC )
# MAGIC THEN UPDATE SET
# MAGIC     target.ProductName = source.ProductName,
# MAGIC     target.Category = source.Category
# MAGIC 
# MAGIC WHEN NOT MATCHED
# MAGIC THEN INSERT (
# MAGIC     ProductKey,
# MAGIC     ProductID,
# MAGIC     ProductName,
# MAGIC     Category
# MAGIC )
# MAGIC VALUES (
# MAGIC     source.ProductKey,
# MAGIC     source.ProductID,
# MAGIC     source.ProductName,
# MAGIC     source.Category
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM DimProduct
# MAGIC ORDER BY ProductKey 

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
