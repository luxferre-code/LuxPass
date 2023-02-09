import sqlite3
import hashlib

class Database:
    def __init__(self, name: str, logger: bool = False) -> None:
        self.__name = name
        self.__logger = logger
        self.__connection = None
        self.__cursor = None
        self.initialize()

    
    def log(self, message: str) -> None:
        """Log message"""
        if self.__logger:
            print(f"[DATABASE]: {message}")

    
    def load(self) -> None:
        """Load database"""
        self.__connection = sqlite3.connect(self.__name)
        self.__cursor = self.__connection.cursor()
        self.__connection.commit()
        self.log("loaded")

    
    def save(self) -> None:
        """Save database"""
        self.__connection.commit()
        self.log("saved")

    
    def close(self) -> None:
        """Close database"""
        self.__connection.close()
        self.log("closed")


    def unload(self) -> None:
        """Unload database"""
        self.save()
        self.close()

    
    def initialize(self) -> None:
        """Initialize database"""
        self.load()
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, name TEXT, password TEXT)")
        self.unload()
        self.log("initialized")


    def add_user(self, username: str, password: str) -> None:
        """Add user to database"""
        self.load()
        self.__cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.unload()
        self.log(f"added user {username}")

    
    def remove_user(self, username: str, password: str) -> None:
        """Remove user from database"""
        self.load()
        self.__cursor.execute("DELETE FROM users WHERE username = ? AND password = ?", (username, password))
        self.unload()
        self.log(f"removed user {username}")

    
    def get_id(self, username: str, password: str) -> int:
        """Get user id"""
        self.load()
        self.__cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        id = self.__cursor.fetchone()
        if id == None:
            return None
        id = id[0]
        self.unload()
        self.log(f"got id {id}")
        return id

    
    def add_password(self, id: int, name: str, password_to_add: str) -> None:
        """Add password to database"""
        self.load()
        self.__cursor.execute("INSERT INTO passwords (user_id, name, password) VALUES (?, ?, ?)", (id, name, password_to_add))
        self.unload()
        self.log(f"added password {name}")

    
    def remove_password(self, id: int, name: str) -> None:
        """Remove password from database"""
        self.load()
        self.__cursor.execute("DELETE FROM passwords WHERE user_id = ? AND name = ?", (id, name))
        self.unload()
        self.log(f"removed password {name}")


    def get_password(self, id: int, name: str) -> str:
        """Get password from database"""
        self.load()
        self.__cursor.execute("SELECT password FROM passwords WHERE user_id = ? AND name = ?", (id, name))
        password = self.__cursor.fetchone()[0]
        self.unload()
        self.log(f"got password {name}")
        return password


    def get_passwords(self, id: int) -> list:
        """Get passwords from database"""
        self.load()
        self.__cursor.execute("SELECT name, password FROM passwords WHERE user_id = ?", (id,))
        passwords = self.__cursor.fetchall()
        self.unload()
        self.log(f"got passwords")
        return passwords


    def name_exists(self, username: str) -> bool:
        """Check if name exists"""
        self.load()
        self.__cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        exists = self.__cursor.fetchone() is not None
        self.unload()
        self.log(f"name exists: {exists}")
        return exists

    
    def change_password(self, id: int, old_password: str, new_password: str) -> None:
        """Change password"""
        self.load()
        self.__cursor.execute("UPDATE users SET password = ? WHERE id = ? AND password = ?", (new_password, id, old_password))
        self.unload()
        self.log(f"changed password")