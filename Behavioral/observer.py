from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class InternetShop(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("InternetShop: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def notification(self):
        print(f"InternetShop: I begin notification")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class EmailAlert(Observer):
    def update(self):
        print("EmailAlert: notification completed")


class SMSAlert(Observer):
    def update(self):
        print("SMSAlert: notification completed")


if __name__ == "__main__":
    internetShop = InternetShop()

    observer_email = EmailAlert()
    internetShop.attach(observer_email)

    observer_sms = SMSAlert()
    internetShop.attach(observer_sms)

    internetShop.notification()

    internetShop.detach(observer_email)

    internetShop.notification()