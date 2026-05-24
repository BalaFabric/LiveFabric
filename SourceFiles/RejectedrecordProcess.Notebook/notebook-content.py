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

testdf = spark.sql(
    '''WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY SalesID, OrderDate, CustomerID, ProductID
               ORDER BY SalesAmount DESC
           ) AS rn
    FROM LandingTable
)
SELECT *
FROM CTE
WHERE rn = 1;
''')
display(testdf)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

testdf.createOrReplaceTempView('LandingfactSales')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col, when, current_timestamp

staging_df = spark.table("LandingfactSales")

dim_customer_df = spark.table("DimCustomer")
dim_product_df = spark.table("DimProduct")
dim_date_df = spark.table("DimDate")

fact_sales_df = spark.table("FactSales")

fact_df = (
    staging_df.alias("s")
    .join(dim_customer_df.alias("c"),
          col("s.CustomerID") == col("c.CustomerID"),
          "inner")
    .join(dim_product_df.alias("p"),
          col("s.ProductID") == col("p.ProductID"),
          "inner")
    .join(dim_date_df.alias("d"),
          col("s.OrderDate") == col("d.FullDate"),
          "inner")
).select(
    col("s.SalesID").alias("SalesID"),
    col("d.DateKey").alias("DateKey"),
    col("c.CustomerKey").alias("CustomerKey"),
    col("p.ProductKey").alias("ProductKey"),
    col("s.Quantity").alias("Quantity"),
    col("s.SalesAmount").alias("SalesAmount")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import row_number, max, coalesce, lit, col
from pyspark.sql.window import Window

window_spec = Window.orderBy("SalesID")

max_key = fact_sales_df \
    .agg(
        coalesce(max("SalesKey"), lit(0)).alias("MaxKey")
    ) \
    .collect()[0]["MaxKey"]
    
fact_final_df = fact_df.select(
    (row_number().over(window_spec) + max_key).alias("SalesKey"),
    col("SalesID"),
    col("DateKey"),
    col("CustomerKey"),
    col("ProductKey"),
    col("Quantity"),
    col("SalesAmount")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col
from pyspark.sql.types import (
    IntegerType,
    DecimalType,
    LongType,
    TimestampType
)

fact_final_df = fact_final_df \
    .withColumn("SalesKey", col("SalesKey").cast(LongType())) \
    .withColumn("SalesID", col("SalesID").cast(IntegerType())) \
    .withColumn("DateKey", col("DateKey").cast(IntegerType())) \
    .withColumn("CustomerKey", col("CustomerKey").cast(LongType())) \
    .withColumn("ProductKey", col("ProductKey").cast(LongType())) \
    .withColumn("Quantity", col("Quantity").cast(IntegerType())) \
    .withColumn("SalesAmount", col("SalesAmount").cast(DecimalType(10,2)))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

fact_final_df.write.mode("append").saveAsTable("FactSales")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC UPDATE FactSales
# MAGIC SET ModifiedDate = (SELECT MAX(OrderDate) FROM LandingfactSales)
# MAGIC WHERE ModifiedDate IS NULL

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC MERGE INTO LandingTable AS L
# MAGIC USING (
# MAGIC     SELECT
# MAGIC         S.CustomerID,
# MAGIC         S.ProductID
# MAGIC     FROM LandingTable S
# MAGIC     INNER JOIN DimCustomer C
# MAGIC         ON S.CustomerID = C.CustomerID
# MAGIC     INNER JOIN DimProduct P
# MAGIC         ON S.ProductID = P.ProductID
# MAGIC ) AS X
# MAGIC ON  L.CustomerID = X.CustomerID
# MAGIC AND L.ProductID  = X.ProductID
# MAGIC 
# MAGIC WHEN MATCHED THEN DELETE;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM FactSales
# MAGIC ORDER BY SalesKey

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
