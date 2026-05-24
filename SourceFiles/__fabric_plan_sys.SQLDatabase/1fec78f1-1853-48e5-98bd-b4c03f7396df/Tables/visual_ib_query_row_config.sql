CREATE TABLE [1fec78f1-1853-48e5-98bd-b4c03f7396df].[visual_ib_query_row_config] (
    [id]        BIGINT         IDENTITY (1, 1) NOT NULL,
    [queryId]   INT            NOT NULL,
    [meta]      NVARCHAR (MAX) NOT NULL,
    [status]    INT            CONSTRAINT [DF_56dff66a22994233932a269dd84] DEFAULT ((10)) NOT NULL,
    [createdBy] NVARCHAR (128) NOT NULL,
    [updatedBy] NVARCHAR (128) NOT NULL,
    [createdAt] INT            NOT NULL,
    [updatedAt] INT            NOT NULL,
    [visualId]  INT            NOT NULL,
    CONSTRAINT [PK_20b024b4bab503df7b8a5b8e014] PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_2748529be79a18a7f9edf1643ac] FOREIGN KEY ([visualId]) REFERENCES [1fec78f1-1853-48e5-98bd-b4c03f7396df].[visual] ([id]),
    CONSTRAINT [FK_abb7599f3b74888c3c397b49cfe] FOREIGN KEY ([queryId]) REFERENCES [1fec78f1-1853-48e5-98bd-b4c03f7396df].[ib_queries] ([id]) ON DELETE CASCADE
);


GO

CREATE NONCLUSTERED INDEX [idx_visual_ib_query_row_config_queryId]
    ON [1fec78f1-1853-48e5-98bd-b4c03f7396df].[visual_ib_query_row_config]([queryId] ASC);


GO

CREATE NONCLUSTERED INDEX [idx_visual_ib_query_row_config_visualId]
    ON [1fec78f1-1853-48e5-98bd-b4c03f7396df].[visual_ib_query_row_config]([visualId] ASC);


GO

