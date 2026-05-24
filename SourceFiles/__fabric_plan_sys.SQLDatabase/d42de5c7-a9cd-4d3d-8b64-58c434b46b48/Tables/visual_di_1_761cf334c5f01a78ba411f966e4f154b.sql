CREATE TABLE [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[visual_di_1_761cf334c5f01a78ba411f966e4f154b] (
    [id]                                    BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                                 NVARCHAR (255)   NOT NULL,
    [colId]                                 NVARCHAR (255)   NOT NULL,
    [scenarioId]                            INT              NULL,
    [filterContextHash]                     NVARCHAR (255)   NULL,
    [updatedAt]                             INT              NOT NULL,
    [updatedBy]                             NVARCHAR (128)   NOT NULL,
    [dim_163eba72c2f9769a62015de3e878c1c30] NVARCHAR (255)   NULL,
    [measure_1]                             DECIMAL (30, 10) NULL,
    [measure_1_meta]                        NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_1_761cf334c5f01a78ba411f966e4f154b_dim_163eba72c2f9769a62015de3e878c1c30]
    ON [d42de5c7-a9cd-4d3d-8b64-58c434b46b48].[visual_di_1_761cf334c5f01a78ba411f966e4f154b]([dim_163eba72c2f9769a62015de3e878c1c30] ASC);


GO

