CREATE TABLE [b754dc9a-d925-4e21-929d-dc88a0612254].[visual_di_4_cedee77d7578a3b1d8fe3944dea2eace] (
    [id]                       BIGINT           IDENTITY (1, 1) NOT NULL,
    [rowId]                    NVARCHAR (255)   NOT NULL,
    [colId]                    NVARCHAR (255)   NOT NULL,
    [scenarioId]               INT              NULL,
    [filterContextHash]        NVARCHAR (255)   NULL,
    [updatedAt]                INT              NOT NULL,
    [updatedBy]                NVARCHAR (128)   NOT NULL,
    [dim_TableModelDataMarket] NVARCHAR (255)   NULL,
    [measure_1]                DECIMAL (30, 10) NULL,
    [measure_1_meta]           NVARCHAR (255)   NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    UNIQUE NONCLUSTERED ([rowId] ASC, [colId] ASC, [scenarioId] ASC, [filterContextHash] ASC)
);


GO

CREATE NONCLUSTERED INDEX [visual_di_4_cedee77d7578a3b1d8fe3944dea2eace_dim_TableModelDataMarket]
    ON [b754dc9a-d925-4e21-929d-dc88a0612254].[visual_di_4_cedee77d7578a3b1d8fe3944dea2eace]([dim_TableModelDataMarket] ASC);


GO

