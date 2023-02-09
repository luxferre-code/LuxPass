from database import Database
from password import *

class Client:
    def __init__(self, username: str, password: str, database: Database) -> None:
        self.__username = username
        self.__password = password
        self.__database = database
        if(self.login(self.__database)):
            self.__id = self.__database.get_id(self.__username, hash_password(self.__password))
        else:
            self.__id = None


    def login(self, database: Database) -> bool:
        """Login to database"""
        return database.get_id(self.__username, hash_password(self.__password)) != None

    
    def __str__(self) -> str:
        return f"Client(username={self.__username}, password={self.__password}, id={self.__id})"


    def get_master_key(self) -> str:
        """Get master key"""
        return self.__password

    
    def get_id(self) -> int:
        """Get id"""
        return self.__id

    
    def get_username(self) -> str:
        """Get username"""
        return self.__username