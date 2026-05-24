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

df = spark.read.csv(path='abfss://TestClass@onelake.dfs.fabric.microsoft.com/DemoLH.Lakehouse/Files/IncrementalDataLoad',header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('EmployeeStaging')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM EmployeeStaging

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS EmpDestination
# MAGIC (
# MAGIC EmpId VARCHAR(100),
# MAGIC EmpName VARCHAR(100),
# MAGIC Salary VARCHAR(100),
# MAGIC DeptName VARCHAR(100),
# MAGIC Location VARCHAR(100),
# MAGIC Country VARCHAR(100)
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col

source_df = spark.table("EmployeeStaging")
target_df = spark.table("EmpDestination")

# Get target count correctly
initial_count = spark.sql("SELECT COUNT(*) AS cnt FROM EmpDestination").collect()[0]["cnt"]
print(initial_count)

if initial_count == 0:
    insert_df = source_df
    update_df = spark.createDataFrame([], source_df.schema)  # empty
    delete_df = spark.createDataFrame([], source_df.schema)  # empty
else:
    # Inserts
    insert_df = source_df.join(target_df, "EmpId", "left_anti")

    # Updates
    update_df = source_df.alias("s").join(target_df.alias("t"), "EmpId") \
        .filter(
            ~(
                (col("s.EmpName").eqNullSafe(col("t.EmpName"))) &
                (col("s.Salary").eqNullSafe(col("t.Salary"))) &
                (col("s.DeptName").eqNullSafe(col("t.DeptName"))) &
                (col("s.Location").eqNullSafe(col("t.Location"))) &
                (col("s.Country").eqNullSafe(col("t.Country")))
            )
        )

    # Deletes
    delete_df = target_df.join(source_df, "EmpId", "left_anti")

# Counts
insert_count = insert_df.count()
update_count = update_df.count()
delete_count = delete_df.count()

print("Insert count:", insert_count)
print("Update count:", update_count)
print("Delete count:", delete_count)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS MergeLogTable
# MAGIC (
# MAGIC RunTime TIMESTAMP,
# MAGIC InsertCount INT,
# MAGIC UpdateCount INT,
# MAGIC DeleteCount INT
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import current_timestamp, col
from pyspark.sql.types import IntegerType

log_df = spark.createDataFrame(
    [(insert_count, update_count, delete_count)],
    ["InsertCount", "UpdateCount", "DeleteCount"]
).withColumn("RunTime", current_timestamp()) \
 .withColumn("InsertCount", col("InsertCount").cast(IntegerType())) \
 .withColumn("UpdateCount", col("UpdateCount").cast(IntegerType())) \
 .withColumn("DeleteCount", col("DeleteCount").cast(IntegerType()))

log_df.write.format("delta").mode("append").saveAsTable("MergeLogTable")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC MERGE INTO EmpDestination AS target
# MAGIC USING EmployeeStaging AS source
# MAGIC ON target.EmpId = source.EmpId
# MAGIC 
# MAGIC WHEN MATCHED AND (
# MAGIC     target.EmpName <> source.EmpName OR
# MAGIC     target.Salary <> source.Salary OR
# MAGIC     target.DeptName <> source.DeptName OR
# MAGIC     target.Location <> source.Location OR
# MAGIC     target.Country <> source.Country
# MAGIC )
# MAGIC THEN UPDATE SET
# MAGIC     target.EmpName = source.EmpName,
# MAGIC     target.Salary = source.Salary,
# MAGIC     target.DeptName = source.DeptName,
# MAGIC     target.Location = source.Location,
# MAGIC     target.Country = source.Country
# MAGIC 
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT (
# MAGIC     EmpId,
# MAGIC     EmpName,
# MAGIC     Salary,
# MAGIC     DeptName,
# MAGIC     Location,
# MAGIC     Country
# MAGIC )
# MAGIC VALUES (
# MAGIC     source.EmpId,
# MAGIC     source.EmpName,
# MAGIC     source.Salary,
# MAGIC     source.DeptName,
# MAGIC     source.Location,
# MAGIC     source.Country
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM EmpDestination

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM MergeLogTable
# MAGIC ORDER BY RunTime DESC

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
