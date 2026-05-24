CREATE TABLE [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[visual_di_6_194c85f40f8d6058f364e4a8ed5ef7d5] (
    [id]                                    BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                                 NVARCHAR (255)   NOT NULL,
    [colId]                                 NVARCHAR (255)   NOT NULL,
    [scenarioId]                            INT              NULL,
    [filterContextHash]                     NVARCHAR (255)   NULL,
    [updatedAt]                             INT              NOT NULL,
    [updatedBy]                             NVARCHAR (128)   NOT NULL,
    [dim_56073b97807ff62e27185aaba8de7b487] NVARCHAR (255)   NULL,
    [measure_20]                            DECIMAL (30, 10) NULL,
    [measure_20_meta]                       NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_6_194c85f40f8d6058f364e4a8ed5ef7d5_dim_56073b97807ff62e27185aaba8de7b487]
    ON [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[visual_di_6_194c85f40f8d6058f364e4a8ed5ef7d5]([dim_56073b97807ff62e27185aaba8de7b487] ASC);


GO

