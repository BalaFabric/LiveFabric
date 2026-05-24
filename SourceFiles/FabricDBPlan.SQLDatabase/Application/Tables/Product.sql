CREATE TABLE [Application].[Product] (
    [ProductID]     INT             NOT NULL,
    [ProductName]   VARCHAR (100)   NULL,
    [Price]         DECIMAL (10, 2) NULL,
    [SubCategoryID] INT             NULL,
    [ValidFrom]     DATETIME2 (0)   NULL,
    PRIMARY KEY CLUSTERED ([ProductID] ASC)
);


GO

