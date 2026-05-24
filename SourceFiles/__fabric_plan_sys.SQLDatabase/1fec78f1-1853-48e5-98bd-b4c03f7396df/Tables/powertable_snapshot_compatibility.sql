CREATE TABLE [1fec78f1-1853-48e5-98bd-b4c03f7396df].[powertable_snapshot_compatibility] (
    [id]                             INT            IDENTITY (1, 1) NOT NULL,
    [sourceId]                       INT            NOT NULL,
    [sourceSnapshotSchemaData]       NVARCHAR (MAX) NULL,
    [sourceSnapshotColumnConfigData] NVARCHAR (MAX) NULL,
    [sourceSnapshotId]               INT            NULL,
    [targetSnapshotId]               INT            NOT NULL,
    [compatibilityStatus]            INT            NOT NULL,
    [compatibilityIssues]            NVARCHAR (MAX) NULL,
    [status]                         INT            NOT NULL,
    [createdAt]                      INT            NOT NULL,
    [updatedAt]                      INT            NOT NULL,
    [createdBy]                      NVARCHAR (128) NOT NULL,
    [updatedBy]                      NVARCHAR (128) NOT NULL,
    CONSTRAINT [PK_679489b8dcdf6deb5c7697e67f1] PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_compat_powertable_source] FOREIGN KEY ([sourceId]) REFERENCES [1fec78f1-1853-48e5-98bd-b4c03f7396df].[powertable_source] ([id]),
    CONSTRAINT [FK_compat_targetSnapshot] FOREIGN KEY ([targetSnapshotId]) REFERENCES [1fec78f1-1853-48e5-98bd-b4c03f7396df].[powertable_snapshot] ([id])
);


GO

