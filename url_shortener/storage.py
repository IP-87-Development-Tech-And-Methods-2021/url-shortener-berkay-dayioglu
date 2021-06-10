from abc import ABC, abstractmethod
from threading import Lock
from typing import Dict, Optional

from tinydb import TinyDB, Query

class PermanentStorage(Storage):
    def __init__():
        self._write_lock: Lock = Lock()
        users = TinyDB('db/users.json')
        User = Query()

    def read_user(self, email: str):
        users.search(User.email == email)

    def add_user(self, email: str, password: str):
        users.insert({"email": email, "password": password, "url_list": {}})

    def remove_user(self, email):
        users.remove(User.email == email)

    def add_url(self, email, url_orig, url_short):
        user_data = users.search(User.email == email)
        user_data.url_list[url_short] = url_orig
        users.update({"url_list": user_data.url_list}, User.email == email)

    def remove_url(self, email, url_short):
        user_data - users.search(User.email == email)
        users_data.url_list.pop("url_short", None)


class InMemoryStorage():
    """ Simple in-memory implementation of key-value storage.
    Note, how it is inherited from abstract `Storage` class
    and implements all its abstract methods. This is done this way
    in order to make some guarantees regarding class public API
    """

    def __init__(self):
        self._write_lock: Lock = Lock()
        self._data: Dict[str, str] = {}

    def read(self, key: str) -> Optional[str]:
        return self._data.get(key)

    def write(self, key: str, value: str):
        with self._write_lock:
            self._data[key] = value
