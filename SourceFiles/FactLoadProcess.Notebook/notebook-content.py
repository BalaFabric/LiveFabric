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

df = spark.read.csv(path='abfss://TestClass@onelake.dfs.fabric.microsoft.com/TestLH.Lakehouse/Files/Development/SalesStaging.csv',header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('StagingSales')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS FactSales
# MAGIC (
# MAGIC     SalesKey BIGINT,
# MAGIC     SalesID INT,
# MAGIC     DateKey INT,
# MAGIC     CustomerKey BIGINT,
# MAGIC     ProductKey BIGINT,
# MAGIC     Quantity INT,
# MAGIC     SalesAmount DECIMAL(10,2),
# MAGIC     ModifiedDate TIMESTAMP
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS LandingTable
# MAGIC (
# MAGIC     SalesID INT,
# MAGIC     OrderDate DATE,
# MAGIC     CustomerID INT,
# MAGIC     ProductID INT,
# MAGIC     Quantity INT,
# MAGIC     SalesAmount DECIMAL(10,2),
# MAGIC     RejectionStatus VARCHAR(1000),
# MAGIC     LoadDate TIMESTAMP
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col, when, current_timestamp

staging_df = spark.table("StagingSales")

dim_customer_df = spark.table("DimCustomer")

dim_product_df = spark.table("DimProduct")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import (
    col,
    when,
    current_timestamp
)

landing_df = (
    staging_df.alias("s")
    .join(
        dim_customer_df.alias("c"),
        col("s.CustomerID") == col("c.CustomerID"),
        "left"
    )
    .join(
        dim_product_df.alias("p"),
        col("s.ProductID") == col("p.ProductID"),
        "left"
    )
    .filter(
        col("c.CustomerKey").isNull() |
        col("p.ProductKey").isNull()
    )
    .select(
        col("s.SalesID").cast("int").alias("SalesID"),
        col("s.OrderDate").cast("date").alias("OrderDate"),
        col("s.CustomerID").cast("int").alias("CustomerID"),
        col("s.ProductID").cast("int").alias("ProductID"),
        col("s.Quantity").cast("int").alias("Quantity"),
        col("s.SalesAmount").cast("decimal(10,2)").alias("SalesAmount"),

        when(
            col("c.CustomerKey").isNull() &
            col("p.ProductKey").isNull(),
            "Customer and Product Missing"

        ).when(
            col("c.CustomerKey").isNull(),
            "Customer Missing"

        ).when(
            col("p.ProductKey").isNull(),
            "Product Missing"

        ).alias("RejectionStatus"),

        current_timestamp().alias("LoadDate")
    )
)

# display(landing_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

landing_df.write.mode("append").saveAsTable("LandingTable")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import max, coalesce, lit, col

# Read Fact Table
fact_sales_df = spark.table("FactSales")

# Get latest OrderDate already loaded
last_order_date = fact_sales_df \
    .agg(
        coalesce(
            max("ModifiedDate"),
            lit("1900-01-01")
        ).alias("MaxDate")
    ) \
    .collect()[0]["MaxDate"]

print(last_order_date)

# Read staging table
staging_df = spark.table("StagingSales")

# Incremental records
incremental_df = staging_df.filter(
    col("OrderDate") > lit(last_order_date)
)

# display(incremental_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

staging_df = spark.table("StagingSales")

dim_customer_df = spark.table("DimCustomer")
dim_product_df = spark.table("DimProduct")
dim_date_df = spark.table("DimDate")

fact_sales_df = spark.table("FactSales")

fact_df = (
    incremental_df.alias("s")
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
# MAGIC SET ModifiedDate = (SELECT MAX(OrderDate) FROM StagingSales)
# MAGIC WHERE ModifiedDate IS NULL

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
