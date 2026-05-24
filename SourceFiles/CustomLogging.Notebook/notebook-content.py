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

PipelineId  = ''
PipelineRunId  = ''
WorkspaceId  = ''
PipelineName  = ''
TriggerType  = ''
TriggerId  = ''
PipelineTriggerByPipelineId = ''
PipelineTriggerByPipelineRunId = ''
PipelineTriggerByPipelineName  = ''
StartDate = ''
EndDate = ''
PipelineExecutionStatus = ''
LogTableName     = ''
TableFormat      = ''
tablemode       = ''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.types import StructType, StructField, StringType

SchemaData = StructType([
    StructField("PipelineId", StringType(), True),
    StructField("PipelineRunId", StringType(), True),
    StructField("WorkspaceId", StringType(), True),
    StructField("PipelineName", StringType(), True),
    StructField("TriggerType", StringType(), True),
    StructField("TriggerId", StringType(), True),
    StructField("PipelineTriggerByPipelineId", StringType(), True),
    StructField("PipelineTriggerByPipelineRunId", StringType(), True),
    StructField("PipelineTriggerByPipelineName", StringType(), True),
    StructField("StartDate", StringType(), True),
    StructField("EndDate", StringType(), True),
    StructField("PipelineExecutionStatus", StringType(), True)
])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

Data = [(
    PipelineId,
    PipelineRunId,
    WorkspaceId,
    PipelineName,
    TriggerType,
    TriggerId,
    PipelineTriggerByPipelineId,
    PipelineTriggerByPipelineRunId,
    PipelineTriggerByPipelineName,
    StartDate,
    EndDate,
    PipelineExecutionStatus
)]

df = spark.createDataFrame(Data, SchemaData)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import Row

Data = [
    Row(
        PipelineId=PipelineId,
        PipelineRunId=PipelineRunId,
        WorkspaceId=WorkspaceId,
        PipelineName=PipelineName,
        TriggerType=TriggerType,
        TriggerId=TriggerId,
        PipelineTriggerByPipelineId=PipelineTriggerByPipelineId,
        PipelineTriggerByPipelineRunId=PipelineTriggerByPipelineRunId,
        PipelineTriggerByPipelineName=PipelineTriggerByPipelineName,
        StartDate=StartDate,
        EndDate=EndDate,
        PipelineExecutionStatus=PipelineExecutionStatus
    )
]

Tempdf = spark.createDataFrame(Data, SchemaData)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

Tempdf.write \
    .format(TableFormat) \
    .mode(tablemode) \
    .saveAsTable(LogTableName)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
