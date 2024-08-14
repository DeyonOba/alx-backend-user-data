"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Saves user to database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs):
        """
        Retrieve the first record that matches the value of each column.

        This method takes in arbitrary keyword  arguments and returns the
        first row found in the `users` table as filtered by the keyword args

        Raise:
            NoResultFound: when record is not withing the table.
            InvalidRequestError: when wrong query arguments are passed.
        """
        users = self._session.query(User)

        for key, value in kwargs.items():

            if key not in User.__dict__:
                raise InvalidRequestError

            for user in users:
                if getattr(user, key) == value:
                    return user
        raise NoResultFound
