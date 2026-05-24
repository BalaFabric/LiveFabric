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

# Welcome to your new notebook
# Type here in the cell editor to add code!
from delta.tables import *
from pyspark.sql.functions import *

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************

lakehousePath = "abfss://POC@onelake.dfs.fabric.microsoft.com/POCLH.Lakehouse/Tables"
tableName = "Category"
tableKey = "ColorID"
dateColumn = "ValidFrom"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

deltaTablePath = f"{lakehousePath}/dbo/{tableName}" #fill in your delta table path 
# print(deltaTablePath)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Get maxdate and number of records in table

# CELL ********************

df = spark.read.format("delta").load(deltaTablePath)
maxdate = df.agg(max(dateColumn)).collect()[0][0]
rowcount = df.count()
# print(maxdate)
maxdate_str = maxdate.strftime("%Y-%m-%d %H:%M:%S")
result = "maxdate="+maxdate_str +  "|rowcount="+str(rowcount)
mssparkutils.notebook.exit(result)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
