create table if not exists jobs
(
    id                  int auto_increment
        primary key,
    priority            int          null,
    code                varchar(500) null,  -- this is used to determine which service can execute which task
    data                json         null,  -- contains the data needed for the agent to execute the task; not relevant for you
    job_state           varchar(150) null,  -- field for storing the state (`running`, `done`, etc...; value is NULL if the job has not yet been executed)
    job_time_started    datetime     null,
    job_time_done       datetime     null,
    channel             varchar(50)  null  -- used to assure a specific execution order. For two jobs with the same `channel`the one with lower priority value and/or lower ID should be executed first
);





-- This is a generic table to specify arbitrary requirements for any execution agent
create table if not exists job_requirements
(
    id                        int auto_increment
        primary key,
    job_id                    int                                null,  -- references JOBS Table
    requirement_name           varchar(255)                       null,
    requirement_value          varchar(255)                       null,
    constraint job_requirements_ibfk_1
        foreign key (job_id) references jobs (id)
);

create index job_id
    on job_requirements (job_id);
    
create index jobs_code_job_state_priority_index
    on jobs (code, job_state, priority);
    
