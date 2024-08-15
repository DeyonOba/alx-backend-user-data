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
        for key, value in kwargs.items():

            if key not in User.__dict__:
                raise InvalidRequestError

        users = self._session.query(User)

        for user in users:
            valid_value = True
            for key, value in kwargs.items():
                if getattr(user, key) != value:
                    valid_value = False
            if valid_value:
                return user

        raise NoResultFound

    def update_user(self, user_id, **kwargs):
        """
        Updates user attributes using the passed arguments method
        """

        try:
            user = self.find_user_by(id=user_id)
        except (InvalidRequestError, NoResultFound):
            raise ValueError

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
                self._session.commit()
            else:
                raise ValueError
