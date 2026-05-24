CREATE TABLE [Application].[SubCategory] (
    [SubCategoryID]   INT           NOT NULL,
    [SubCategoryName] VARCHAR (100) NULL,
    [CategoryID]      INT           NULL,
    [ValidFrom]       DATETIME2 (0) NULL,
    PRIMARY KEY CLUSTERED ([SubCategoryID] ASC)
);


GO

