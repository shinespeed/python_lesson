import telebot
from threading import Thread
from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def responce_message(self):
        pass


class TelegramView(View):
    _token = "1124654910:AAG3whPcDrG8cCtaA9ESQApYUrRKhVJqJ_8"
    _bot = telebot.TeleBot(_token)
    Thread(target=_bot.polling, args=(True,)).start()

    @_bot.message_handler(commands=['start'])
    def start(self, message):
        sent = self._bot.send_message(message.chat.id, str)

    def responce_message(self, string: str, id_chat: int):
        self._bot.send_message(id_chat, string)


class Model:
    _chat_id = 402919227
    _string = ''
    _als_string = 'this modify model'

    def __init__(self, string: str):
        self._string = string + ' + ' + self._als_string

    def change_exstra_str(self, string: str):
        self._als_string = string

    def set_string(self, string: str):
        self._string = string + ' + ' + self._als_string

    @property
    def get_string(self):
        return self._string

    def set_chat_id(self, chat_id: int):
        self._chat_id = chat_id

    @property
    def get_chat_id(self):
        return self._chat_id


class Controller:
    _model: Model
    _view: View

    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def update_view(self):
        self._view.responce_message(self._model.get_string, self._model.get_chat_id)


class MVC:
    _view = TelegramView()
    _model = Model('TEST')
    _controller = Controller(_model, _view)

    def __init__(self):
        self.write_message()

    def write_message(self):
        while True:
            self._model.set_string(input("Write message: "))
            self._controller.update_view()


if __name__ == "__main__":
    mvc = MVC()