"""interface for container"""
from abc import ABCMeta, abstractmethod


class AbstractUserManager(metaclass=ABCMeta):
    # pylint: disable=too-few-public-methods
    """user manager interface"""
    @abstractmethod
    def authenticate(self, username: str, password: str):
        """get user object"""
        return None

    @abstractmethod
    def register(self, username: str, password: str) -> bool:
        """register user object"""
        return False

    @abstractmethod
    def delete(self, user) -> bool:
        """delete user"""
        return False
