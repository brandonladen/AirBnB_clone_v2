#!/usr/bin/python3
"""
Dbengine to store in the MySQL database
"""
import sqlalchemy
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    """this class is the engine to store
    mysql database
    """
    # set a private class attribute
    __engine = None
    __session = None

    def __init__(self):
        """
        initialize the db engine
        """
        # defined variables
        USER = getenv('HBNB_MYSQL_USER')
        PASSWORD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENVN = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER,
            PASSWORD,
            HOST,
            DB), pool_pre_ping=True)
        if ENVN == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        show the requested data from database
        Query on the current database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj
        """
        List = {}
        classes = {
            'State': State, 'City': City,
            'Amenity': Amenity, 'User': User,
            'Place': Place, 'Review': Review}

        if cls is not None:
            objects = self.__session.query(cls).all()
            for obj in objects:
                List[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            for clas, value in classes.items():
                objects = self.__session.query(value).all()
                for obj in objects:
                    List[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return List

    def new(self, obj):
        """add ond or update data to database"""
        self.__session.add(obj)

    def save(self):
        """save the added data"""
        self.__session.commit()

    def delete(self, obj=None):
        """remove data from db"""
        self.__session.delete(obj)

    def reload(self):
        """create all reload data
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(
            session_factory)

    def close(self):
        """call remove() method on the private session attribute
        (self.__session) tips or close() on the class Session"""
        self.__session.close()
