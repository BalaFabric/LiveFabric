CREATE TABLE [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_di_5_d827ca54eb8c7654da05f68898e37295] (
    [id]                              BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                           NVARCHAR (255)   NOT NULL,
    [colId]                           NVARCHAR (255)   NOT NULL,
    [scenarioId]                      INT              NULL,
    [filterContextHash]               NVARCHAR (255)   NULL,
    [updatedAt]                       INT              NOT NULL,
    [updatedBy]                       NVARCHAR (128)   NOT NULL,
    [dim_TableModelDataCategory]      NVARCHAR (255)   NULL,
    [dim_TableModelDataOrderPriority] NVARCHAR (255)   NULL,
    [measure_10]                      DECIMAL (30, 10) NULL,
    [measure_10_meta]                 NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_5_d827ca54eb8c7654da05f68898e37295_dim_TableModelDataCategory]
    ON [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_di_5_d827ca54eb8c7654da05f68898e37295]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_di_5_d827ca54eb8c7654da05f68898e37295_dim_TableModelDataOrderPriority]
    ON [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_di_5_d827ca54eb8c7654da05f68898e37295]([dim_TableModelDataOrderPriority] ASC);


GO

