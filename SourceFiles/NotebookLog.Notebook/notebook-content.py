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

import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FabricNotebook")

def log_to_table(step, status, message):
    data = [(step, status, message, datetime.now())]
    columns = ["Step", "Status", "Message", "LogTime"]
    
    df_log = spark.createDataFrame(data, columns)
    df_log.write.format("delta").mode("append").saveAsTable("NotebookLogTable")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def log_step(step_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"{step_name} started")
                log_to_table(step_name, "Started", f"{step_name} started")

                result = func(*args, **kwargs)

                logger.info(f"{step_name} completed")
                log_to_table(step_name, "Success", f"{step_name} completed")

                return result

            except Exception as e:
                logger.error(f"{step_name} failed: {str(e)}")
                log_to_table(step_name, "Failed", str(e))
                raise e
        return wrapper
    return decorator

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

@log_step("Read CSV File")
def read_data():
    return spark.read.csv("abfss://TestClass@onelake.dfs.fabric.microsoft.com/DemoLH.Lakehouse/Files/Development/Emp.csv")

@log_step("Write to Table")
def write_data(df):
    df.write.format("delta").mode("append").saveAsTable("TargetTable")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = read_data()
write_data(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM NotebookLogTable
# MAGIC ORDER BY LogTime ASC

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import logging
from datetime import datetime
from notebookutils import notebook

notebook_status = "SUCCESS"

# Logging function
def log_to_table(step, status, message):
    data = [(step, status, message, datetime.now())]
    df = spark.createDataFrame(data, ["Step", "Status", "Message", "LogTime"])
    df.write.format("delta").mode("append").saveAsTable("NotebookLogTable")

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FabricNotebook")

try:
    logger.info("Starting notebook")

    df = spark.read.csv("abfss://TestClass@onelake.dfs.fabric.microsoft.com/DemoLH.Lakehouse/Files/Development/Emp.csv")
    log_to_table("Read", "Success", "Data read successfully")

    # Example step
    df.write.format("delta").mode("append").saveAsTable("TargetTable")
    log_to_table("Write", "Success", "Data written successfully")

except Exception as e:
    notebook_status = "FAILED"
    logger.error(f"Notebook failed: {str(e)}")
    log_to_table("Notebook", "Failed", str(e))

finally:
    logger.info(f"Final Status: {notebook_status}")
    log_to_table("Notebook", notebook_status, f"Final Status: {notebook_status}")

    # 🔥 THIS IS WHAT YOU WERE ASKING
    notebook.exit(notebook_status)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
