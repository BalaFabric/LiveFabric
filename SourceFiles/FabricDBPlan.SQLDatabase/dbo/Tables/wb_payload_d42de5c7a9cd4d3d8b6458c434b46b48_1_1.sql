CREATE TABLE [dbo].[wb_payload_d42de5c7a9cd4d3d8b6458c434b46b48_1_1] (
    [Shipmode]          VARCHAR (MAX)  NULL,
    [Region]            VARCHAR (MAX)  NULL,
    [ValueColumnName]   NVARCHAR (512) NULL,
    [Value]             NVARCHAR (MAX) NULL,
    [Source]            NVARCHAR (512) NULL,
    [IrNotes]           NVARCHAR (MAX) NULL,
    [IrScenario]        NVARCHAR (512) NULL,
    [CellId]            VARCHAR (MAX)  NULL,
    [IsAggregated]      TINYINT        CONSTRAINT [wb_payload_d42de5c7a9cd4d3d8b6458c434b46b48_1_1_isaggregated_default] DEFAULT ('1') NULL,
    [FilterContextHash] VARCHAR (MAX)  NULL,
    [ExecutionId]       NVARCHAR (512) NULL,
    [IrId]              NVARCHAR (512) NULL
);


GO

