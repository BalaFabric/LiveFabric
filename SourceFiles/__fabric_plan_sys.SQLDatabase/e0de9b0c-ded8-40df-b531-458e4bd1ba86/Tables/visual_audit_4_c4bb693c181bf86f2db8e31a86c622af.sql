CREATE TABLE [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_audit_4_c4bb693c181bf86f2db8e31a86c622af] (
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
    [dim_TableModelDataCategory] NVARCHAR (255)  NULL,
    [dim_TableModelDataMarket]   NVARCHAR (255)  NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_audit_4_c4bb693c181bf86f2db8e31a86c622af_dim_TableModelDataCategory]
    ON [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_audit_4_c4bb693c181bf86f2db8e31a86c622af]([dim_TableModelDataCategory] ASC);


GO

CREATE NONCLUSTERED INDEX [visual_audit_4_c4bb693c181bf86f2db8e31a86c622af_dim_TableModelDataMarket]
    ON [e0de9b0c-ded8-40df-b531-458e4bd1ba86].[visual_audit_4_c4bb693c181bf86f2db8e31a86c622af]([dim_TableModelDataMarket] ASC);


GO

