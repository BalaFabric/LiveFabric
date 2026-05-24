CREATE TABLE [dbo].[PipelineExecutionLog] (

	[Id] bigint IDENTITY NOT NULL, 
	[PipelineId] varchar(100) NULL, 
	[PipelineRunId] varchar(100) NULL, 
	[WorkspaceId] varchar(100) NULL, 
	[PipelineName] varchar(255) NULL, 
	[TriggerType] varchar(100) NULL, 
	[TriggerId] varchar(100) NULL, 
	[PipelineTriggerByPipelineId] varchar(100) NULL, 
	[PipelineTriggerByPipelineRunId] varchar(100) NULL, 
	[PipelineTriggerByPipelineName] varchar(255) NULL, 
	[StartDate] varchar(100) NULL, 
	[EndDate] varchar(100) NULL, 
	[PipelineExecutionStatus] varchar(50) NULL
);