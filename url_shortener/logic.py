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
        t_email = t.Email
        t_pwd   = t.String(min_length=6, max_length=63)

    # TODO: add logging
    #       finish trafaret checking
    def read_user(email: str):
        return self._storage.read_user(email)
    def add_user(email:str, password: str):
        try:
            t_email.check(email)
            t_pwd.check(password)
            self._storage.add_user(email, password)
            return True
        except:
            return False

    def remove_user(email:str):
        self._storage.remove_user(email, password)

    def read_url(email:str, url_short: str):
        self._storage.
    def add_url(email:str, url_short: str, url_orig: str):
        self._storage.add_url(email, url_short, url_orig)
    def remove_url(email:str, url_short: str):
        self._storage.remove_url(email, url_short)

    def add_token(email: str):
        tokens = self._storage_mem.read(email)
        if tokens is not None:
            return False
        tokens[email] = urandom(128)
        self._storage_mem.write(tokens)
        return True
    def remove_token(email: str): 
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
