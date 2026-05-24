CREATE TABLE [8b1cd269-1a83-4bf2-ae1d-ec4132af6b38].[visual_di_1_6b7a1c0c1c53bdaff964553f6901c860] (
    [id]                         BIGINT         IDENTITY (1, 1) NOT NULL,
    [rowId]                      NVARCHAR (255) NOT NULL,
    [colId]                      NVARCHAR (255) NOT NULL,
    [scenarioId]                 INT            NULL,
    [filterContextHash]          NVARCHAR (255) NULL,
    [updatedAt]                  INT            NOT NULL,
    [updatedBy]                  NVARCHAR (128) NOT NULL,
    [dim_TableModelDataSegment]  NVARCHAR (255) NULL,
    [dim_TableModelDataCategory] NVARCHAR (255) NULL,
    [measure_1]                  NVARCHAR (MAX) NULL,
    [measure_1_meta]             NVARCHAR (255) NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_1_6b7a1c0c1c53bdaff964553f6901c860_dim_TableModelDataCategory]
    ON [8b1cd269-1a83-4bf2-ae1d-ec4132af6b38].[visual_di_1_6b7a1c0c1c53bdaff964553f6901c860]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_di_1_6b7a1c0c1c53bdaff964553f6901c860_dim_TableModelDataSegment]
    ON [8b1cd269-1a83-4bf2-ae1d-ec4132af6b38].[visual_di_1_6b7a1c0c1c53bdaff964553f6901c860]([dim_TableModelDataSegment] ASC);


GO

