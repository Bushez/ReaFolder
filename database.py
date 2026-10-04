from models.base import Base
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

class Database():
    @staticmethod
    def start(drop_all = False):
        engine = create_engine("sqlite:///db", echo=True)

        @event.listens_for(engine, "connect")
        def enable_foreign_keys(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.close()

        SessionF = sessionmaker(engine)
        if drop_all:
            Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        return SessionF


