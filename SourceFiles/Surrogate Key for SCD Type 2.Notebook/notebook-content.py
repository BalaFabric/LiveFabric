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

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS SourceTableData (
# MAGIC     EmpId INT,
# MAGIC     EmpName VARCHAR(100),
# MAGIC     Salary INT,
# MAGIC     DeptName VARCHAR(100),
# MAGIC     Location VARCHAR(100),
# MAGIC     Country VARCHAR(100)
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS DestinationTableData (
# MAGIC     SurrogateKey INT,
# MAGIC     EmpId INT,
# MAGIC     EmpName VARCHAR(100),
# MAGIC     Salary INT,
# MAGIC     DeptName VARCHAR(100),
# MAGIC     Location VARCHAR(100),
# MAGIC     Country VARCHAR(100),
# MAGIC     StartDate DATE,
# MAGIC     EndDate DATE,
# MAGIC     Active_Indicator CHAR(1),
# MAGIC     InsertedDateTime DATE,
# MAGIC     UpdatedDatetime DATE,
# MAGIC     Action VARCHAR(50)
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS Temp_Destination (
# MAGIC     SurrogateKey INT,
# MAGIC     EmpId INT,
# MAGIC     EmpName VARCHAR(100),
# MAGIC     Salary INT,
# MAGIC     DeptName VARCHAR(100),
# MAGIC     Location VARCHAR(100),
# MAGIC     Country VARCHAR(100),
# MAGIC     StartDate DATE,
# MAGIC     EndDate DATE,
# MAGIC     Active_Indicator CHAR(1),
# MAGIC     InsertedDateTime DATE,
# MAGIC     UpdatedDatetime DATE,
# MAGIC     Action VARCHAR(50)
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DestinationTableData
# MAGIC SELECT 
# MAGIC     ROW_NUMBER() OVER(ORDER BY Src.EmpId) + COALESCE((SELECT MAX(SurrogateKey) FROM DestinationTableData),0) AS SurrogateKey,
# MAGIC     Src.EmpId,
# MAGIC     Src.EmpName,
# MAGIC     Src.Salary,
# MAGIC     Src.DeptName,
# MAGIC     Src.Location,
# MAGIC     Src.Country,
# MAGIC     current_date,
# MAGIC     DATE '9999-12-31',
# MAGIC     'Y',
# MAGIC     current_date,
# MAGIC     NULL,
# MAGIC     'INSERT'
# MAGIC FROM SourceTableData Src
# MAGIC LEFT JOIN DestinationTableData Dst
# MAGIC ON Src.EmpId = Dst.EmpId
# MAGIC WHERE Dst.EmpId IS NULL;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO Temp_Destination
# MAGIC SELECT 
# MAGIC     ROW_NUMBER() OVER(ORDER BY Src.EmpId) + COALESCE((SELECT MAX(SurrogateKey) FROM DestinationTableData),0),
# MAGIC     Src.EmpId,
# MAGIC     Src.EmpName,
# MAGIC     Src.Salary,
# MAGIC     Src.DeptName,
# MAGIC     Src.Location,
# MAGIC     Src.Country,
# MAGIC     current_date,
# MAGIC     DATE '9999-12-31',
# MAGIC     'Y',
# MAGIC     current_date,
# MAGIC     NULL,
# MAGIC     'INSERT'
# MAGIC FROM DestinationTableData Dst
# MAGIC INNER JOIN SourceTableData Src
# MAGIC ON Dst.EmpId = Src.EmpId
# MAGIC WHERE 
# MAGIC     (Dst.EmpName <> Src.EmpName OR 
# MAGIC      Dst.Salary <> Src.Salary OR
# MAGIC      Dst.DeptName <> Src.DeptName OR
# MAGIC      Dst.Location <> Src.Location OR
# MAGIC      Dst.Country <> Src.Country)
# MAGIC AND Dst.Active_indicator = 'Y';

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC MERGE INTO DestinationTableData Dst
# MAGIC USING SourceTableData Src
# MAGIC ON Src.EmpId = Dst.EmpId
# MAGIC AND Dst.Active_indicator = 'Y'
# MAGIC 
# MAGIC WHEN MATCHED AND (
# MAGIC     Dst.EmpName <> Src.EmpName OR
# MAGIC     Dst.Salary <> Src.Salary OR
# MAGIC     Dst.DeptName <> Src.DeptName OR
# MAGIC     Dst.Location <> Src.Location OR
# MAGIC     Dst.Country <> Src.Country
# MAGIC )
# MAGIC 
# MAGIC THEN UPDATE SET
# MAGIC     Dst.EndDate = current_date() - 1,
# MAGIC     Dst.Active_indicator = 'N',
# MAGIC     Dst.UpdatedDatetime = current_date(),
# MAGIC     Dst.Action = 'UPDATE';
# MAGIC 	
# MAGIC 	%%sql
# MAGIC INSERT INTO DestinationTableData
# MAGIC SELECT * FROM Temp_Destination;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


%%sql
DELETE FROM Temp_Destination

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM DestinationTableData
# MAGIC ORDER BY SurrogateKey

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
