CREATE TABLE [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[visual_audit_6_0fa69b3b72dc0c204c7fb2b2fab53f01] (
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
    [dim_5527fd520f994f9dfe45dc70ec244b806] NVARCHAR (255)  NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_audit_6_0fa69b3b72dc0c204c7fb2b2fab53f01_dim_5527fd520f994f9dfe45dc70ec244b806]
    ON [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[visual_audit_6_0fa69b3b72dc0c204c7fb2b2fab53f01]([dim_5527fd520f994f9dfe45dc70ec244b806] ASC);


GO

