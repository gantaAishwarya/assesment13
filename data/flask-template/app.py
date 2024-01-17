import os
import uuid
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, jsonify
from database import get_database
from flask_restful import Api
from src.list_available_jobs import ListJobs
from src.pick_for_execution import PickJob
app = Flask(__name__)


def execute_sql_file(file_path, session):
    with open(file_path, 'r') as sql_file:
        sql_statements = sql_file.read()

    for statement in sql_statements.split(');'):
        if statement == sql_statements.split(');')[-1]:
            session.execute(statement)
        else:
            session.execute(statement+");")
        
    session.commit()

# this is executed once at startup
with app.app_context():
    db_engine = get_database()
    with sessionmaker(bind=db_engine)() as local_session:
        # TODO: setup database and insert data
        execute_sql_file("data/CREATE_TABLES.sql",local_session)
        execute_sql_file("data/INSERT_DATA.sql",local_session)
        #local_session.execute(sql_script)
        #local_session.commit()


# TODO: add API Endpoints
api = Api(app)
api.add_resource(ListJobs,'/api/listJobs')
api.add_resource(PickJob,'/api/pickJob')

#TODO: add anothe resource to read job done status and update job done time
if __name__ == '__main__':
    app.run()
