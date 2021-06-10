import trafaret as t

from threading import Lock
from typing import Optional
from os import urandom

from url_shortener.storage import PermanentStorage, InMemoryStorage
from url_shortener.dto import User


class Logic:
    """This class implements application logic"""

    def __init__(self, storage: PermanentStorage, storage_mem: InMemoryStorage):
        self._storage: PermanentStorage = storage
        self._storage_mem: InMemoryStorage = storage_mem
        self._check_and_write_lock: Lock = Lock()
        self.t_email = t.Email
        self.t_pwd   = t.String(min_length=6, max_length=63)

    # TODO: add logging
    #       finish trafaret checking
    def read_user(self, email: str):
        return self._storage.read_user(email)

    def add_user(self, email:str, password: str):
        try:
            self.t_email.check(email)
            self.t_pwd.check(password)
        except:
            print("password or email not fulfilling requirements")
            return False
        self._storage.add_user(email, password)
        return True

    def remove_user(self, email:str):
        self._storage.remove_user(email, password)

    # def read_url(email:str, url_short: str):
    #    self._storage.read_url(
    def add_url(self, email:str, url_short: str, url_orig: str):
        self._storage.add_url(email, url_short, url_orig)
    def remove_url(self, email:str, url_short: str):
        self._storage.remove_url(email, url_short)

    def add_token(self, email: str):
        tokens = self._storage_mem._data
        if tokens.get(email) is not None:
            return False
        self._storage_mem.write(email, urandom(128))
        return True
    def remove_token(self, email: str): 
        tokens = self._storage_mem.read(email)
        if tokens is None:
            return False
        tokens.pop(email)
        self._storage_mem.write(tokens)
        return True

    def find_user_by_token(self, token: str) -> Optional[User]:
        # TODO: implement actual checking logic
        if token.strip():
            return User(email='implementme@example.com')
        return None
