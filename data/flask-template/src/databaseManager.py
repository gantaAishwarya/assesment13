from flask import jsonify
import json

class DatabaseManager:
    def __init__(self):
        # Constructor for the DatabaseManager class
        # You can perform database initializations here
        pass

    def __finally__(self):
        # Cleanup method; if you need to close connections or cursors, you can implement it here
        pass

    def readData(self, path):
        with open(path, 'r') as json_file:
                data = json.load(json_file)
        return data
     

    def getAllJobs(self):
        # Method for retrieving all jobs 
        print('[DatabaseManager.py] [getAllJobs] retrieving all jobs')
        try:
            jobs = self.readData("data/INSERT_JOB_DATA.json")
            print(jobs)
            #filtering available jobs
            available_jobs = [job for job in jobs if job.get("job_state") == None]
            return available_jobs
        except Exception as e:
            return 'ERROR!! ' + str(e)


    def pickJob(self):
        # Method for retrieving all jobs 
        print('[DatabaseManager.py] [pickJob] retrieving all jobs')

        try:
            jobs = self.readData("data/INSERT_JOB_DATA.json")

            job_requirements = self.readData("data/INSERT_REQU_DATA.json")

            available_jobs = [job for job in jobs if job.get("job_state") != "Done"]

            # Get a set of job IDs present in job_requirements
            required_job_ids = set(req.get("job_id") for req in job_requirements)
        
            
            # Filter available jobs based on the condition
            filtered_jobs = [job for job in available_jobs if job.get("id") in required_job_ids]

            #TODO: Filter based on agent code 
            print(filtered_jobs)

            ## Sorting jobs based on priority and channel
            #sorted_jobs = sorted(filtered_jobs, key=lambda job: job.get("priority", 1))
            for job in filtered_jobs:
                # Perform actions for each job
                job_id = job.get("id")
                job_priority = job.get("priority")
                job_code = job.get("code")
                job_data = job.get("data")
                # Retrieve job requirements corresponding to the job ID
                corresponding_requirements = [req for req in job_requirements if req.get("job_id") == job_id]

                for requirement in corresponding_requirements:
                    requirement_name = requirement.get("requirement_name")
                    requirement_value = requirement.get("requirement_value")
                    print(f"Requirement: {requirement_name} - Value: {requirement_value}")
                    #TODO: Check if requirements met or not
                    met = True

                if(met):
                    job["job_state"] = "In-Progress"
                    return job
            

        except Exception as e:
            return 'ERROR!! ' + str(e)




