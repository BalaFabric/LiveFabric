CREATE TABLE [dbo].[DeptTest] (
    [EmpID]       INT             IDENTITY (1, 1) NOT NULL,
    [EmpCode]     VARCHAR (20)    NULL,
    [EmpName]     VARCHAR (100)   NOT NULL,
    [Gender]      VARCHAR (10)    NULL,
    [Department]  VARCHAR (50)    NULL,
    [Salary]      DECIMAL (10, 2) NULL,
    [City]        VARCHAR (50)    NULL,
    [ManagerID]   INT             NULL,
    [Email]       VARCHAR (100)   NULL,
    [IsActive]    VARCHAR (100)   NULL,
    [HireDate]    DATE            NULL,
    [CreatedDate] DATETIME        DEFAULT (getdate()) NULL,
    PRIMARY KEY CLUSTERED ([EmpID] ASC),
    UNIQUE NONCLUSTERED ([EmpCode] ASC)
);


GO

