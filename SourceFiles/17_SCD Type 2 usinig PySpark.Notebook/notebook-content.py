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
# MAGIC CREATE TABLE SourceTableData (
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
# MAGIC INSERT INTO SourceTableData (EmpId, EmpName, Salary, DeptName, Location, Country) 
# MAGIC VALUES 
# MAGIC     (1, 'Ramu', 67, 'Sales', 'Chennai', 'USA'),
# MAGIC     (2, 'Srinu', 654, 'HR', 'Bangalore', 'India'),
# MAGIC     (3, 'Venkat', 23, 'IT', 'Hyderabad', 'UK')

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM SourceTableData

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC UPDATE SourceTableData
# MAGIC SET EmpName = 'Demo Fabric'
# MAGIC WHERE EmpId = 1

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE TABLE DestinationTableData (
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
# MAGIC CREATE TABLE Temp_Destination (
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
# MAGIC 	MERGE INTO DestinationTableData Dst
# MAGIC 			USING SourceTableData Src
# MAGIC 		ON (Src.EmpId = Dst.EmpId) AND Dst.Active_indicator = 'Y'
# MAGIC 		 WHEN NOT MATCHED BY TARGET THEN 
# MAGIC 		  INSERT 
# MAGIC 		 (  
# MAGIC 			EmpId,
# MAGIC 			EmpName,
# MAGIC 			Salary,
# MAGIC 			DeptName,
# MAGIC 			Location,
# MAGIC 			Country,
# MAGIC 			StartDate,
# MAGIC 			ENDDATE,
# MAGIC 			Active_indicator,
# MAGIC 			InsertedDateTime,
# MAGIC 			UpdatedDatetime ,
# MAGIC 			ACTION
# MAGIC 		 ) 
# MAGIC 		VALUES
# MAGIC 		(
# MAGIC 			Src.EmpId,
# MAGIC 			Src.EmpName,
# MAGIC 			Src.Salary,
# MAGIC 			Src.DeptName,
# MAGIC 			Src.Location,
# MAGIC 			Src.Country,
# MAGIC 			current_date,
# MAGIC 			CAST('9999-12-31' AS TIMESTAMP),
# MAGIC       		'Y',
# MAGIC 			current_date,
# MAGIC 			NULL,
# MAGIC 			'INSERT'
# MAGIC 		)

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO Temp_Destination
# MAGIC SELECT Src.EmpId,
# MAGIC                             Src.EmpName,
# MAGIC                             Src.Salary,
# MAGIC                             Src.DeptName,
# MAGIC                             Src.Location,
# MAGIC                             Src.Country,
# MAGIC                             current_date,
# MAGIC                             CAST('9999-12-31' AS TIMESTAMP),
# MAGIC                             'Y',
# MAGIC                             current_date,
# MAGIC                             NULL,
# MAGIC                             'INSERT'
# MAGIC                         FROM 
# MAGIC                         DestinationTableData Dst 
# MAGIC                         INNER JOIN SourceTableData Src
# MAGIC                         ON Dst.EmpId = Src.EmpId
# MAGIC                         WHERE 	   ( Dst.EmpName    <> Src.EmpName OR 
# MAGIC                                     Dst.Salary <> Src.Salary OR
# MAGIC                                     Dst.DeptName   <> Src.DeptName OR
# MAGIC                                     Dst.Location     <> Src.Location OR
# MAGIC                                     Dst.Country     <> Src.Country ) AND  Dst.Active_indicator = 'Y'

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 			MERGE INTO DestinationTableData Dst
# MAGIC 			USING (SELECT Src.EmpId,
# MAGIC                             Src.EmpName,
# MAGIC                             Src.Salary,
# MAGIC                             Src.DeptName,
# MAGIC                             Src.Location,
# MAGIC                             Src.Country,
# MAGIC                             current_date,
# MAGIC                             NULL,
# MAGIC                             'Y',
# MAGIC                             current_date,
# MAGIC                             NULL,
# MAGIC                             'INSERT'
# MAGIC                         FROM 
# MAGIC                         DestinationTableData Dst 
# MAGIC                         INNER JOIN SourceTableData Src
# MAGIC                         ON Dst.EmpId = Src.EmpId
# MAGIC                         WHERE 	   ( Dst.EmpName    <> Src.EmpName OR 
# MAGIC                                     Dst.Salary <> Src.Salary OR
# MAGIC                                     Dst.DeptName   <> Src.DeptName OR
# MAGIC                                     Dst.Location     <> Src.Location OR
# MAGIC                                     Dst.Country     <> Src.Country ) AND  Dst.Active_indicator = 'Y' ) Src
# MAGIC 		ON (Src.EmpId = Dst.EmpId) AND Dst.Active_indicator = 'Y'
# MAGIC 		WHEN MATCHED AND
# MAGIC 			Dst.EmpName    <> Src.EmpName OR 
# MAGIC 			Dst.Salary <> Src.Salary OR
# MAGIC 			Dst.DeptName   <> Src.DeptName OR
# MAGIC 			Dst.Location     <> Src.Location OR
# MAGIC 			Dst.Country     <> Src.Country OR
# MAGIC 	 		Dst.Active_indicator = 'Y'
# MAGIC 		THEN UPDATE
# MAGIC 		   SET   Dst.ENDDATE = current_date-1,
# MAGIC 				 Dst.Active_indicator = 'N',
# MAGIC 				 Dst.UpdatedDatetime = current_date,
# MAGIC 				 Dst.Action = 'UPDATE'

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO DestinationTableData
# MAGIC SELECT * FROM Temp_Destination

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DELETE FROM Temp_Destination

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM DestinationTableData

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
