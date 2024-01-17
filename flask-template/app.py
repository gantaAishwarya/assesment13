import uuid
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, jsonify

app = Flask(__name__)

# this is executed once at startup
with app.app_context():
    db_engine = get_database()
    with sessionmaker(bind=db_engine)() as local_session:
        # TODO: setup database and insert data
        local_session.execute("CREATE TABLE IF NOT EXISTS ...")
        local_session.commit()


# TODO: add API Endpoints


if __name__ == '__main__':
    app.run()
