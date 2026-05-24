CREATE TABLE [dbo].[Sales] (
    [EmpID]     INT           IDENTITY (1, 1) NOT NULL,
    [EmpCode]   VARCHAR (20)  NOT NULL,
    [FirstName] VARCHAR (50)  NULL,
    [LastName]  VARCHAR (50)  NULL,
    [Location]  VARCHAR (100) NULL,
    [Country]   VARCHAR (50)  NULL,
    [StartDate] DATE          NULL,
    [EndDate]   DATE          NULL,
    [IsActive]  VARCHAR (10)  NULL,
    PRIMARY KEY CLUSTERED ([EmpID] ASC)
);


GO

