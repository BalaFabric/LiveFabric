CREATE TABLE [d0bbf63b-4628-410a-9bfa-7da9e75d682a].[cube_jobs] (
    [id]        INT            IDENTITY (1, 1) NOT NULL,
    [jobId]     VARCHAR (255)  NOT NULL,
    [visualId]  INT            NULL,
    [jobType]   INT            NOT NULL,
    [jobMeta]   NVARCHAR (MAX) NULL,
    [errorMeta] NVARCHAR (MAX) NULL,
    [status]    INT            CONSTRAINT [DF_cube_jobs_status] DEFAULT ((10)) NOT NULL,
    [createdBy] NVARCHAR (128) NOT NULL,
    [updatedBy] NVARCHAR (128) NOT NULL,
    [createdAt] INT            NOT NULL,
    [updatedAt] INT            NOT NULL,
    CONSTRAINT [PK_cube_jobs] PRIMARY KEY CLUSTERED ([id] ASC)
);


GO

