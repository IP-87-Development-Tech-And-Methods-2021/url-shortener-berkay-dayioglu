from url_shortener.storage import PermanentStorage
from url_shortener.storage import InMemoryStorage
from url_shortener.logic import Logic


def test_logic_fails_to_save_when_key_already_exists():
    storage = PermanentStorage()
    storage_mem = InMemoryStorage()
    logic = Logic(storage=storage, storage_mem=storage_mem)

    logic.add_token("test")
    assert logic.read_token("test") is not None
    assert logic.add_token("test") is False
