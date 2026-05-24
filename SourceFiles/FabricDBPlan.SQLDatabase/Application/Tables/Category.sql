CREATE TABLE [Application].[Category] (
    [CategoryID]   INT           NOT NULL,
    [CategoryName] VARCHAR (100) NULL,
    [ValidFrom]    DATETIME2 (0) NULL,
    PRIMARY KEY CLUSTERED ([CategoryID] ASC)
);


GO

