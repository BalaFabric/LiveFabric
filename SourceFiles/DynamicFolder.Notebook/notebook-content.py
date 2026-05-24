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

# PARAMETERS CELL ********************

SourceFolderName    = ""
ArchiveFolderName   = ""
FailedFolderName    = ""
LogTableName        = ""
FileSchemaTableName = ""
FileLogTableName    = ""
TableFormat         = ""
ModeOption          = ""
DataLoadSchema      = ""
DataTableName       = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from datetime import datetime
from notebookutils import mssparkutils
from pyspark.sql.functions import current_timestamp, lit
from pyspark.sql.types import *
import time


# =====================================================
# STEP 1 : BASE PATHS
# =====================================================

base_path = "abfss://TestClass@onelake.dfs.fabric.microsoft.com/DemoLH.Lakehouse/Files"

source_path = f"{base_path}/{SourceFolderName}"

now = datetime.now()

date_path = f"{now.strftime('%Y')}/{now.strftime('%m')}/{now.strftime('%d')}"

raw_path = f"{base_path}/{ArchiveFolderName}/{date_path}"

failed_path = f"{base_path}/{FailedFolderName}/{date_path}"

# =====================================================
# CHECK SOURCE
# =====================================================

if not mssparkutils.fs.exists(source_path):

    print(f"{SourceFolderName} folder does not exist")

    mssparkutils.notebook.exit("failed")

files = [f for f in mssparkutils.fs.ls(source_path) if not f.isDir]

if len(files) == 0:

    print("No files available")

    mssparkutils.notebook.exit("failed")

print(f"Files available for processing : {len(files)}")

# =====================================================
# CREATE FOLDERS
# =====================================================

for path in [raw_path, failed_path]:

    if not mssparkutils.fs.exists(path):

        mssparkutils.fs.mkdirs(path)

time.sleep(2)

# =====================================================
# SCHEMA FROM TABLE
# =====================================================

schema_query = f"""
SELECT ColumnName,
       Columnposition,
       DataType
FROM {FileSchemaTableName}
ORDER BY Columnposition
"""

schema_df = spark.sql(schema_query)

expected_columns = [r["ColumnName"] for r in schema_df.collect()]

print("Expected Columns :", expected_columns)

# =====================================================
# DYNAMIC SCHEMA BUILD
# =====================================================

fields = []

for r in schema_df.collect():

    col = r["ColumnName"]

    dtype = r["DataType"].upper()

    if "INT" in dtype:
        t = IntegerType()

    elif "BIGINT" in dtype:
        t = LongType()

    elif "DOUBLE" in dtype:
        t = DoubleType()

    elif "FLOAT" in dtype:
        t = FloatType()

    elif "DATE" in dtype:
        t = DateType()

    elif "TIMESTAMP" in dtype:
        t = TimestampType()

    else:
        t = StringType()

    fields.append(StructField(col, t, True))

emp_schema = StructType(fields)

# =====================================================
# LOG SCHEMA
# =====================================================

log_schema = StructType([
    StructField("FileName", StringType(), True),
    StructField("RecordCount", IntegerType(), True),
    StructField("ProcessStatus", StringType(), True),
    StructField("ErrorMessage", StringType(), True)
])

is_failed = False

# =====================================================
# PROCESS FILES
# =====================================================

for file in files:

    file_path = file.path

    try:

        print(f"\nProcessing File : {file.name}")

        # =====================================================
        # HEADER VALIDATION
        # =====================================================

        header_df = spark.read.format("csv") \
            .option("header", "true") \
            .load(file_path)

        incoming_columns = header_df.columns

        print("Incoming Columns :", incoming_columns)

        # =====================================================
        # INVALID FILE
        # =====================================================

        if incoming_columns != expected_columns:

            print(f"INVALID FILE : {file.name}")

            spark.createDataFrame([
                (
                    file.name,
                    0,
                    "Failed",
                    f"Schema mismatch Expected {expected_columns} Got {incoming_columns}"
                )
            ], log_schema) \
            .withColumn("ProcessDateTime", current_timestamp()) \
            .write.format(TableFormat) \
            .mode(ModeOption) \
            .saveAsTable(FileLogTableName)

            is_failed = True

            ts = datetime.now().strftime("%Y%m%d%H%M%S")

            mssparkutils.fs.mv(
                file_path,
                f"{failed_path}/{file.name}_{ts}.csv",
                True
            )

            continue

        # =====================================================
        # VALID FILE
        # =====================================================

        df = spark.read.format("csv") \
            .option("header", "true") \
            .schema(emp_schema) \
            .load(file_path)

        final_df = df.withColumn(
            "LoadDate",
            current_timestamp()
        ).withColumn(
            "SourceFileName",
            lit(file.name)
        )

        record_count = final_df.count()

        # =====================================================
        # LOAD DATA
        # =====================================================

        final_df.write \
            .format(TableFormat) \
            .mode(ModeOption) \
            .saveAsTable(DataTableName)

        print(f"Data Loaded Successfully : {file.name}")

        # =====================================================
        # SUCCESS LOG
        # =====================================================

        spark.createDataFrame([
            (
                file.name,
                record_count,
                "Success",
                None
            )
        ], log_schema) \
        .withColumn("ProcessDateTime", current_timestamp()) \
        .write.format(TableFormat) \
        .mode(ModeOption) \
        .saveAsTable(FileLogTableName)

        ts = datetime.now().strftime("%Y%m%d%H%M%S")

        mssparkutils.fs.mv(
            file_path,
            f"{raw_path}/{file.name}_{ts}.csv",
            True
        )

        print("File moved to RAW folder")

    except Exception as e:

        print(f"ERROR FILE : {file.name}")

        print(str(e))

        spark.createDataFrame([
            (
                file.name,
                0,
                "Failed",
                str(e)
            )
        ], log_schema) \
        .withColumn("ProcessDateTime", current_timestamp()) \
        .write.format(TableFormat) \
        .mode(ModeOption) \
        .saveAsTable(FileLogTableName)

        is_failed = True

        ts = datetime.now().strftime("%Y%m%d%H%M%S")

        mssparkutils.fs.mv(
            file_path,
            f"{failed_path}/{file.name}_{ts}.csv",
            True
        )

# =====================================================
# FINAL STATUS
# =====================================================

if is_failed:

    mssparkutils.notebook.exit("failed")

else:

    mssparkutils.notebook.exit("success")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
