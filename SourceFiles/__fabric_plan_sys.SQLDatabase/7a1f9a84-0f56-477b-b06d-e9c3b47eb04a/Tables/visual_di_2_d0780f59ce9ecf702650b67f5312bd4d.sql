CREATE TABLE [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_d0780f59ce9ecf702650b67f5312bd4d] (
    [id]                              BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                           NVARCHAR (255)   NOT NULL,
    [colId]                           NVARCHAR (255)   NOT NULL,
    [scenarioId]                      INT              NULL,
    [filterContextHash]               NVARCHAR (255)   NULL,
    [updatedAt]                       INT              NOT NULL,
    [updatedBy]                       NVARCHAR (128)   NOT NULL,
    [dim_TableModelDataMarket]        NVARCHAR (255)   NULL,
    [dim_TableModelDataOrderPriority] NVARCHAR (255)   NULL,
    [dim_TableModelDataCategory]      NVARCHAR (255)   NULL,
    [measure_2]                       DECIMAL (30, 10) NULL,
    [measure_2_meta]                  NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_2_d0780f59ce9ecf702650b67f5312bd4d_dim_TableModelDataCategory]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_d0780f59ce9ecf702650b67f5312bd4d]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_di_2_d0780f59ce9ecf702650b67f5312bd4d_dim_TableModelDataMarket]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_d0780f59ce9ecf702650b67f5312bd4d]([dim_TableModelDataMarket] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_di_2_d0780f59ce9ecf702650b67f5312bd4d_dim_TableModelDataOrderPriority]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_d0780f59ce9ecf702650b67f5312bd4d]([dim_TableModelDataOrderPriority] ASC);


GO

