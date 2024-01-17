import json
import requests
from flask import request
from flask_restful import Resource
from .initialiseManager import databaseManager

class PickJob(Resource):
    """
        Handle HTTP GET requests to pick job that needs to be executed.
    """
    def get(self):
        print('[app.py] [/PickJob] got request')
        try:
            # Call the databaseManager to get next job
            print('[app.py] [/PickJob] calling databaseManager PickJob')
            #TODO: take agent code as input and validate
            res = databaseManager.pickJob()
            if len(res)!=0:
                # Return the retrieved job as JSON response with a status code of 200 (OK)
                return res, 200
            else:
                # Return an empty list as a JSON response with a status code of 200 (OK)
                return [], 200
        except Exception as e:
            # If an exception is raised, print an error message
            print('ERRORR!! [app.py] [PickJob]' + str(e))
            # Return an error response
            return 'ERROR'