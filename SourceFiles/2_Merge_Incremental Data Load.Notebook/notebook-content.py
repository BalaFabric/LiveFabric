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
# MAGIC CREATE TABLE Employee_Source (
# MAGIC     EmpID INT ,
# MAGIC     EmpName VARCHAR(50),
# MAGIC     Department VARCHAR(50),
# MAGIC     Salary INT,
# MAGIC     LastModified DATE
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO Employee_Source VALUES
# MAGIC (1, 'Ramesh', 'IT', 50000, '2024-01-01'),
# MAGIC (2, 'Suresh', 'HR', 40000, '2024-01-01'),
# MAGIC (3, 'Mahesh', 'Finance', 60000, '2024-01-01');


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM Employee_Source

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC UPDATE Employee_Source
# MAGIC SET Salary = 55000,
# MAGIC     Department = 'Fabric Data Engineering'
# MAGIC WHERE EmpID = 1;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO Employee_Source VALUES
# MAGIC (55, 'Rithvik', 'IT', 50000, '2024-01-01')

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE Employee_Target (
# MAGIC     EmpID INT,
# MAGIC     EmpName VARCHAR(50),
# MAGIC     Department VARCHAR(50),
# MAGIC     Salary INT,
# MAGIC     LastModified DATE
# MAGIC );


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC MERGE INTO Employee_Target AS T
# MAGIC USING Employee_Source AS S
# MAGIC ON T.EmpID = S.EmpID
# MAGIC 
# MAGIC -- UPDATE existing records if data changed
# MAGIC WHEN MATCHED 
# MAGIC      AND (
# MAGIC           T.EmpName <> S.EmpName OR
# MAGIC           T.Department <> S.Department OR
# MAGIC           T.Salary <> S.Salary
# MAGIC          )
# MAGIC THEN
# MAGIC     UPDATE SET
# MAGIC         T.EmpName = S.EmpName,
# MAGIC         T.Department = S.Department,
# MAGIC         T.Salary = S.Salary,
# MAGIC         T.LastModified = S.LastModified
# MAGIC 
# MAGIC -- INSERT new records
# MAGIC WHEN NOT MATCHED BY TARGET
# MAGIC THEN
# MAGIC     INSERT (EmpID, EmpName, Department, Salary, LastModified)
# MAGIC     VALUES (S.EmpID, S.EmpName, S.Department, S.Salary, S.LastModified);


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM Employee_Target

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
