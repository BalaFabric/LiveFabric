CREATE TABLE [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[powertable_approval_filter_sync_logs] (
    [id]         INT            IDENTITY (1, 1) NOT NULL,
    [approvalId] INT            NOT NULL,
    [meta]       NVARCHAR (MAX) NOT NULL,
    [errorMsg]   NVARCHAR (MAX) NULL,
    [status]     INT            NOT NULL,
    [createdBy]  NVARCHAR (128) NOT NULL,
    [updatedBy]  NVARCHAR (128) NOT NULL,
    [createdAt]  INT            NOT NULL,
    [updatedAt]  INT            NOT NULL,
    CONSTRAINT [PK_9366cad86c47bb89df427864217] PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_c853e65e969e2795b8888dcc1ce] FOREIGN KEY ([approvalId]) REFERENCES [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[powertable_approval] ([id])
);


GO

