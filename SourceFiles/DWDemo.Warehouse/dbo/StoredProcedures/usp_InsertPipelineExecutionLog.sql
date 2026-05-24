CREATE PROCEDURE usp_InsertPipelineExecutionLog
(
    @PipelineId VARCHAR(100),
    @PipelineRunId VARCHAR(100),
    @WorkspaceId VARCHAR(100),
    @PipelineName VARCHAR(255),
    @TriggerType VARCHAR(100),
    @TriggerId VARCHAR(100),
    @PipelineTriggerByPipelineId VARCHAR(100),
    @PipelineTriggerByPipelineRunId VARCHAR(100),
    @PipelineTriggerByPipelineName VARCHAR(255),
    @StartDate VARCHAR(100),
    @EndDate VARCHAR(100),
    @PipelineExecutionStatus VARCHAR(50)
)
AS
BEGIN

    SET NOCOUNT ON;

    INSERT INTO PipelineExecutionLog
    (
        PipelineId,
        PipelineRunId,
        WorkspaceId,
        PipelineName,
        TriggerType,
        TriggerId,
        PipelineTriggerByPipelineId,
        PipelineTriggerByPipelineRunId,
        PipelineTriggerByPipelineName,
        StartDate,
        EndDate,
        PipelineExecutionStatus
    )
    VALUES
    (
        @PipelineId,
        @PipelineRunId,
        @WorkspaceId,
        @PipelineName,
        @TriggerType,
        @TriggerId,
        @PipelineTriggerByPipelineId,
        @PipelineTriggerByPipelineRunId,
        @PipelineTriggerByPipelineName,
        @StartDate,
        @EndDate,
        @PipelineExecutionStatus
    );

END;