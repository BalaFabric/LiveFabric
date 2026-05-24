CREATE TABLE [DW].[Customer] (
    [CustomerID]     INT           NOT NULL,
    [CustomerName]   VARCHAR (100) NULL,
    [Email]          VARCHAR (100) NULL,
    [City]           VARCHAR (50)  NULL,
    [Country]        VARCHAR (50)  NULL,
    [LastEditedWhen] DATETIME2 (0) NULL,
    PRIMARY KEY CLUSTERED ([CustomerID] ASC)
);


GO

