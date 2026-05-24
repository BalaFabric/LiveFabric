CREATE TABLE [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_audit_2_eb8afa5cbbd4b9542d6cd0b36aad0c92] (
    [id]                         BIGINT          IDENTITY (1, 1) NOT NULL,
    [rowId]                      NVARCHAR (2048) NOT NULL,
    [colId]                      NVARCHAR (2048) NOT NULL,
    [scenarioGuid]               NVARCHAR (255)  NULL,
    [measureGuid]                NVARCHAR (255)  NULL,
    [filterContextHash]          NVARCHAR (255)  NULL,
    [action]                     NVARCHAR (255)  NULL,
    [meta]                       NVARCHAR (MAX)  NULL,
    [oldValue]                   NVARCHAR (MAX)  NULL,
    [newValue]                   NVARCHAR (MAX)  NULL,
    [updatedAt]                  INT             NOT NULL,
    [updatedByUPN]               NVARCHAR (320)  NOT NULL,
    [updatedBy]                  NVARCHAR (128)  NOT NULL,
    [dim_TableModelDataMarket]   NVARCHAR (255)  NULL,
    [dim_TableModelDataCategory] NVARCHAR (255)  NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_audit_2_eb8afa5cbbd4b9542d6cd0b36aad0c92_dim_TableModelDataCategory]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_audit_2_eb8afa5cbbd4b9542d6cd0b36aad0c92]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_audit_2_eb8afa5cbbd4b9542d6cd0b36aad0c92_dim_TableModelDataMarket]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_audit_2_eb8afa5cbbd4b9542d6cd0b36aad0c92]([dim_TableModelDataMarket] ASC);


GO

