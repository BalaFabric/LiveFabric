CREATE TABLE [Sales].[SalesOrder] (
    [SalesOrderID] INT             NOT NULL,
    [OrderDate]    DATE            NULL,
    [CustomerID]   INT             NULL,
    [TotalAmount]  DECIMAL (12, 2) NULL,
    [ValidFrom]    DATETIME2 (0)   NULL,
    PRIMARY KEY CLUSTERED ([SalesOrderID] ASC)
);


GO

