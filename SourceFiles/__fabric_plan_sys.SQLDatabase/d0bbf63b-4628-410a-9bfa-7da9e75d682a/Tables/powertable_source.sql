CREATE TABLE [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[powertable_source] (
    [id]             INT            IDENTITY (1, 1) NOT NULL,
    [dbName]         VARCHAR (255)  NOT NULL,
    [dbHost]         VARCHAR (255)  NOT NULL,
    [tableName]      VARCHAR (255)  NOT NULL,
    [schemaName]     NVARCHAR (MAX) NULL,
    [tableType]      INT            NULL,
    [meta]           NVARCHAR (MAX) NULL,
    [creationMode]   INT            NULL,
    [fileImportType] INT            NULL,
    [status]         INT            CONSTRAINT [DF_2b063b5739be18a99e045032c12] DEFAULT ((10)) NOT NULL,
    [createdBy]      NVARCHAR (128) NOT NULL,
    [updatedBy]      NVARCHAR (128) NOT NULL,
    [createdAt]      INT            NOT NULL,
    [updatedAt]      INT            NOT NULL,
    [connectionId]   VARCHAR (255)  NOT NULL,
    CONSTRAINT [PK_4fb18167f2d83b6fdfb6980a9df] PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

