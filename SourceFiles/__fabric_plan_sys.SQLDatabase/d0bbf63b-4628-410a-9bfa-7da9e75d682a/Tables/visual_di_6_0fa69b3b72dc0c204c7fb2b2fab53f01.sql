CREATE TABLE [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[visual_di_6_0fa69b3b72dc0c204c7fb2b2fab53f01] (
    [id]                                    BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                                 NVARCHAR (255)   NOT NULL,
    [colId]                                 NVARCHAR (255)   NOT NULL,
    [scenarioId]                            INT              NULL,
    [filterContextHash]                     NVARCHAR (255)   NULL,
    [updatedAt]                             INT              NOT NULL,
    [updatedBy]                             NVARCHAR (128)   NOT NULL,
    [dim_5527fd520f994f9dfe45dc70ec244b806] NVARCHAR (255)   NULL,
    [measure_20]                            DECIMAL (30, 10) NULL,
    [measure_20_meta]                       NVARCHAR (255)   NULL,
    [measure_22]                            NVARCHAR (MAX)   NULL,
    [measure_22_meta]                       NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_6_0fa69b3b72dc0c204c7fb2b2fab53f01_dim_5527fd520f994f9dfe45dc70ec244b806]
    ON [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[visual_di_6_0fa69b3b72dc0c204c7fb2b2fab53f01]([dim_5527fd520f994f9dfe45dc70ec244b806] ASC);


GO

