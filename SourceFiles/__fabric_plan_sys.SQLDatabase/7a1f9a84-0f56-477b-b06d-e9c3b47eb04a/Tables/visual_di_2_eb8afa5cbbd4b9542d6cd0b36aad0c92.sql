CREATE TABLE [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_eb8afa5cbbd4b9542d6cd0b36aad0c92] (
    [id]                         BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                      NVARCHAR (255)   NOT NULL,
    [colId]                      NVARCHAR (255)   NOT NULL,
    [scenarioId]                 INT              NULL,
    [filterContextHash]          NVARCHAR (255)   NULL,
    [updatedAt]                  INT              NOT NULL,
    [updatedBy]                  NVARCHAR (128)   NOT NULL,
    [dim_TableModelDataMarket]   NVARCHAR (255)   NULL,
    [dim_TableModelDataCategory] NVARCHAR (255)   NULL,
    [measure_2]                  DECIMAL (30, 10) NULL,
    [measure_2_meta]             NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_2_eb8afa5cbbd4b9542d6cd0b36aad0c92_dim_TableModelDataCategory]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_eb8afa5cbbd4b9542d6cd0b36aad0c92]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_di_2_eb8afa5cbbd4b9542d6cd0b36aad0c92_dim_TableModelDataMarket]
    ON [7a1f9a84-0f56-477b-b06d-e9c3b47eb04a].[visual_di_2_eb8afa5cbbd4b9542d6cd0b36aad0c92]([dim_TableModelDataMarket] ASC);


GO

