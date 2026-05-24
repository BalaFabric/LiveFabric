CREATE TABLE [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_di_4_c4bb693c181bf86f2db8e31a86c622af] (
    [id]                         BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                      NVARCHAR (255)   NOT NULL,
    [colId]                      NVARCHAR (255)   NOT NULL,
    [scenarioId]                 INT              NULL,
    [filterContextHash]          NVARCHAR (255)   NULL,
    [updatedAt]                  INT              NOT NULL,
    [updatedBy]                  NVARCHAR (128)   NOT NULL,
    [dim_TableModelDataCategory] NVARCHAR (255)   NULL,
    [dim_TableModelDataMarket]   NVARCHAR (255)   NULL,
    [measure_5]                  DECIMAL (30, 10) NULL,
    [measure_6]                  DECIMAL (30, 10) NULL,
    [measure_5_meta]             NVARCHAR (255)   NULL,
    [measure_6_meta]             NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_4_c4bb693c181bf86f2db8e31a86c622af_dim_TableModelDataCategory]
    ON [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_di_4_c4bb693c181bf86f2db8e31a86c622af]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_di_4_c4bb693c181bf86f2db8e31a86c622af_dim_TableModelDataMarket]
    ON [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_di_4_c4bb693c181bf86f2db8e31a86c622af]([dim_TableModelDataMarket] ASC);


GO

