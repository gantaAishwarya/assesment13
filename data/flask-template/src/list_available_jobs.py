import json
import requests
from flask import request
from flask_restful import Resource
from .initialiseManager import databaseManager

class ListJobs(Resource):
    """
        Handle HTTP GET requests to list all available jobs.
    """

    def get(self):
        print('[app.py] [/ListJobs] got request')
        try:
            # Call the databaseManager to fetch all jobs
            print('[app.py] [/ListJobs] calling databaseManager ListJobs')
            res = databaseManager.getAllJobs()
            print(res)
            if len(res)!=0:
                # Return the retrieved jobs as JSON response with a status code of 200 (OK)
                return res, 200
            else:
                # Return an empty list as a JSON response with a status code of 200 (OK)
                return [], 200
        except Exception as e:
            # If an exception is raised, print an error message
            print('ERRORR!! [app.py] [ListJobs]' + str(e))
            # Return an error response
            return 'ERROR'