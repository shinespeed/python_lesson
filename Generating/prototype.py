import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    def clone(self):
        pass


class TelegramBot(Prototype):
    def __init__(self, id, token):
        self._token = token
        self._id = id

    def clone(self):
        obj = TelegramBot(self._id, self._token)
        return obj

    @property
    def get_token(self):
        return self._token

    @property
    def get_id(self):
        return self._id


class ViberBot(Prototype):
    def __init__(self, id, token):
        self._token = token
        self._id = id

    def clone(self):
        obj = ViberBot(self._id, self._token)
        return obj

    @property
    def get_token(self):
        return self._token

    @property
    def get_id(self):
        return self._id


if __name__ == "__main__":
    tel = TelegramBot(12, 55)
    am = tel.clone()
    print(am.get_id)