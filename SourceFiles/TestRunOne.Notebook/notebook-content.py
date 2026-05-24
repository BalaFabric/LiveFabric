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
# META     },
# META     "environment": {
# META       "environmentId": "a8c2336b-b30a-9e76-49f0-bd8ea2512997",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

  DataValue = [(101, 'Venkat', 'Male', 343, 'HR Dept'),
            (102, 'Suresh', 'Female', 234, 'HR Dept'),
            (103, 'Pavani', 'Female', 7900, 'IT Dept'),
            (104, 'Rajesh', 'Male', 8767, 'Marketing Dept'),
            (105, 'Rithvik', 'Female', 4545, 'Finance Dept'),
            (106, 'Sravani', 'Male', 3434, 'Sales Dept'),
            (107, 'Bala', 'Male', 34, 'HR Dept'),
            (108, 'Subbu', 'Female', 3434, 'IT Dept'),
            (109, 'Malli', 'Female', 6767, 'Marketing Dept'),
            (110, 'Ravi', 'Female', 4343, 'Finance Dept'),
            (111, 'Anitha', 'Male', 4545, 'Sales Dept'),
            (112, 'Praveen', 'Male', 3334, 'HR Dept'),
            (113, 'Rao', 'Female', 2333, 'IT Dept'),
            (114, 'Hero', 'Female', 343,'Marketing Dept'),
            (115, 'Super', 'Male', 343, 'Finance Dept')]
SchemaValue = ["EmpId","EmpName","EmpGender","EmpSalary","EmpDept"]
df = spark.createDataFrame(data=DataValue,schema=SchemaValue)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

  DataValue = [(101, 'Venkat', 'Male', 343, 'HR Dept'),
            (102, 'Suresh', 'Female', 234, 'HR Dept'),
            (103, 'Pavani', 'Female', 7900, 'IT Dept'),
            (104, 'Rajesh', 'Male', 8767, 'Marketing Dept'),
            (105, 'Rithvik', 'Female', 4545, 'Finance Dept'),
            (106, 'Sravani', 'Male', 3434, 'Sales Dept'),
            (107, 'Bala', 'Male', 34, 'HR Dept'),
            (108, 'Subbu', 'Female', 3434, 'IT Dept'),
            (109, 'Malli', 'Female', 6767, 'Marketing Dept'),
            (110, 'Ravi', 'Female', 4343, 'Finance Dept'),
            (111, 'Anitha', 'Male', 4545, 'Sales Dept'),
            (112, 'Praveen', 'Male', 3334, 'HR Dept'),
            (113, 'Rao', 'Female', 2333, 'IT Dept'),
            (114, 'Hero', 'Female', 343,'Marketing Dept'),
            (115, 'Super', 'Male', 343, 'Finance Dept')]
SchemaValue = ["EmpId","EmpName","EmpGender","EmpSalary","EmpDept"]
TestDF = spark.createDataFrame(data=DataValue,schema=SchemaValue)
display(TestDF)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format('delta').mode('append').saveAsTable('ScheduleNotebook')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
