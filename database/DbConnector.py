import flask
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from database import user, password, host, dbname


# Database Connector ↓
class DbConnect:
    __db: SQLAlchemy
    __engine: sqlalchemy.engine.base.Engine
    __Base: sqlalchemy.ext.declarative.api.DeclarativeMeta
    __session_factory: sessionmaker
    __session: scoped_session
    # noinspection PyUnresolvedReferences
    __metadata: sqlalchemy.sql.schema.MetaData

    def __init__(self):
        # Configurations ↓
        self.SQLALCHEMY_DATABASE_URI: str = f'mysql+pymysql://{user}:{password}@{host}/{dbname}'
        self.SQLALCHEMY_POOL_SIZE: int = 20
        self.SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
        self.SQLALCHEMY_ENGINE_OPTIONS: dict = {
            'pool_pre_ping': True,
            'pool_recycle': 1,
        }

    def connect(self, app: flask.app.Flask):
        # Database Objects ↓
        self.__db = SQLAlchemy(app)
        self.__engine = self.__db.engine
        self.__Base = declarative_base(self.__engine)
        self.__metadata = self.__db.metadata

        # Database Session ↓
        self.__session_factory = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(self.__session_factory)

    def getEngine(self):
        return self.__engine

    def getBase(self):
        return self.__Base

    def getMetadata(self):
        return self.__metadata

    def getSession(self):
        return self.__session()


if __name__ == '__main__':
    print('Hello World')
