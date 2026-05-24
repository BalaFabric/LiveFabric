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

from delta.tables import *
from pyspark.sql.functions import *

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************

lakehousePath = "abfss://TestClass@onelake.dfs.fabric.microsoft.com/DemoLH.Lakehouse"
tableName = "Customer"
tableKey = "CustomerID"
tableKey2 = None
dateColumn = "LastEditedWhen"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# deltaTablePath = f"{lakehousePath}/Tables/{tableName}" 
deltaTablePath = f"{lakehousePath}/Tables/dbo/{tableName}" 
# print(deltaTablePath)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

parquetFilePath = f"{lakehousePath}/Files/incremental/{tableName}/{tableName}.parquet"
# print(parquetFilePath)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df2 = spark.read.parquet(parquetFilePath)
# display(df2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

if tableKey2 is None:
    mergeKeyExpr = f"t.{tableKey} = s.{tableKey}"
else:
    mergeKeyExpr = f"t.{tableKey} = s.{tableKey} AND t.{tableKey2} = s.{tableKey2}"    

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Check if table already exists; if it does, do an upsert and return how many rows were inserted and update; if it does not exist, return how many rows were inserted

# CELL ********************

from delta.tables import DeltaTable

if DeltaTable.isDeltaTable(spark, deltaTablePath):
    deltaTable = DeltaTable.forPath(spark, deltaTablePath)

    (
        deltaTable.alias("t")
        .merge(
            df2.alias("s"),
            mergeKeyExpr
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )

    history = deltaTable.history(1).select("operationMetrics").collect()[0]
    operationMetrics = history["operationMetrics"]

    numInserted = int(operationMetrics.get("numTargetRowsInserted", 0))
    numUpdated  = int(operationMetrics.get("numTargetRowsUpdated", 0))
    print(numUpdated)

else:
    df2.write.format("delta").mode("append").save(deltaTablePath)

    numInserted = df2.count()
    numUpdated  = 0


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Get the latest date loaded into the table - this will be used for watermarking; return the max date, the number of rows inserted and number updated

# CELL ********************

deltaTablePath = f"{lakehousePath}/Tables/dbo/{tableName}"
df3 = spark.read.format("delta").load(deltaTablePath)
maxdate = df3.agg(max(dateColumn)).collect()[0][0]
# print(maxdate)
maxdate_str = maxdate.strftime("%Y-%m-%d %H:%M:%S")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

result = "maxdate="+maxdate_str +  "|numInserted="+str(numInserted)+  "|numUpdated="+str(numUpdated)
# result = {"maxdate": maxdate_str, "numInserted": numInserted, "numUpdated": numUpdated}
mssparkutils.notebook.exit(str(result))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

