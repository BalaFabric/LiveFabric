CREATE TABLE [b754dc9a-d925-4e21-929d-dc88a0612254].[powertable_snapshot_restore_job] (
    [id]               INT            IDENTITY (1, 1) NOT NULL,
    [sourceId]         INT            NOT NULL,
    [sourceSnapshotId] INT            NOT NULL,
    [targetSnapshotId] INT            NULL,
    [startTime]        INT            NULL,
    [endTime]          INT            NULL,
    [errorMsg]         NVARCHAR (MAX) NULL,
    [status]           INT            NOT NULL,
    [createdAt]        INT            NOT NULL,
    [updatedAt]        INT            NOT NULL,
    [createdBy]        NVARCHAR (128) NOT NULL,
    [updatedBy]        NVARCHAR (128) NOT NULL,
    CONSTRAINT [PK_a5c64521ab9e22726ec7db40394] PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_restore_powertable_source] FOREIGN KEY ([sourceId]) REFERENCES [b754dc9a-d925-4e21-929d-dc88a0612254].[powertable_source] ([id]),
    CONSTRAINT [FK_restore_sourceSnapshot] FOREIGN KEY ([sourceSnapshotId]) REFERENCES [b754dc9a-d925-4e21-929d-dc88a0612254].[powertable_snapshot] ([id])
);


GO

