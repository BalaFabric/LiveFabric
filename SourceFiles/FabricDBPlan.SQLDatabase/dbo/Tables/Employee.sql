CREATE TABLE [dbo].[Employee] (
    [EmpID]       INT             NOT NULL,
    [EmpName]     VARCHAR (50)    NULL,
    [Gender]      VARCHAR (10)    NULL,
    [Salary]      DECIMAL (10, 2) NULL,
    [Department]  VARCHAR (50)    NULL,
    [EmpLocation] VARCHAR (255)   DEFAULT ('Hyderabad') NOT NULL,
    PRIMARY KEY CLUSTERED ([EmpID] ASC)
);


GO

