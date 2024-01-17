from sqlalchemy import create_engine

db = None


def get_database():
    global db
    if db is None:
        db = _create_db_mock()
    return db


def _create_db_mock():
    # You can also use a real database here by just replacing the in-memory connection string by one to a local MySQL-Database
    connection_string = "sqlite:///:memory:"
    engine = create_engine(connection_string, echo=False, pool_pre_ping=True)
    return engine
