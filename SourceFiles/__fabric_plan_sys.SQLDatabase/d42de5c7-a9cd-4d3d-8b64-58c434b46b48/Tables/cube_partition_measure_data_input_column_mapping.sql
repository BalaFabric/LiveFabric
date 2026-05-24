CREATE TABLE [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[cube_partition_measure_data_input_column_mapping] (
    [id]                     INT            IDENTITY (1, 1) NOT NULL,
    [cubePartitionMeasureId] INT            NOT NULL,
    [dataInputColumnId]      INT            NOT NULL,
    [visualId]               INT            NOT NULL,
    [status]                 INT            CONSTRAINT [DF_5432ffc8ab91bb9ef728cbf7164] DEFAULT ((10)) NOT NULL,
    [createdBy]              NVARCHAR (128) NOT NULL,
    [updatedBy]              NVARCHAR (128) NOT NULL,
    [createdAt]              INT            NOT NULL,
    [updatedAt]              INT            NOT NULL,
    CONSTRAINT [PK_ec9340f040f65d90be690c1f75d] PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_5ca3b59ef2e04877a66a426e02c] FOREIGN KEY ([visualId]) REFERENCES [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[visual] ([id]),
    CONSTRAINT [FK_5e6a165e3b8d3bb9abe6e156e61] FOREIGN KEY ([cubePartitionMeasureId]) REFERENCES [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[cube_partition_measure] ([id]),
    CONSTRAINT [FK_9a898dd0c3447c80396fc066ee3] FOREIGN KEY ([dataInputColumnId]) REFERENCES [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[data_input_column] ([id])
);


GO

