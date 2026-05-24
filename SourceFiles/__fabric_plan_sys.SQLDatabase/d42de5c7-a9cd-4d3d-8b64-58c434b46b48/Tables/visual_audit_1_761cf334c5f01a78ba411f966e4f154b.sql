CREATE TABLE [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[visual_audit_1_761cf334c5f01a78ba411f966e4f154b] (
    [id]                                    BIGINT          IDENTITY (1, 1) NOT NULL,
    [rowId]                                 NVARCHAR (2048) NOT NULL,
    [colId]                                 NVARCHAR (2048) NOT NULL,
    [scenarioGuid]                          NVARCHAR (255)  NULL,
    [measureGuid]                           NVARCHAR (255)  NULL,
    [filterContextHash]                     NVARCHAR (255)  NULL,
    [action]                                NVARCHAR (255)  NULL,
    [meta]                                  NVARCHAR (MAX)  NULL,
    [oldValue]                              NVARCHAR (MAX)  NULL,
    [newValue]                              NVARCHAR (MAX)  NULL,
    [updatedAt]                             INT             NOT NULL,
    [updatedByUPN]                          NVARCHAR (320)  NOT NULL,
    [updatedBy]                             NVARCHAR (128)  NOT NULL,
    [dim_163eba72c2f9769a62015de3e878c1c30] NVARCHAR (255)  NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_audit_1_761cf334c5f01a78ba411f966e4f154b_dim_163eba72c2f9769a62015de3e878c1c30]
    ON [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[visual_audit_1_761cf334c5f01a78ba411f966e4f154b]([dim_163eba72c2f9769a62015de3e878c1c30] ASC);


GO

