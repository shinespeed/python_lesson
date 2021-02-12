from abc import ABC, abstractmethod


class DataBaseInterface(ABC):
    @abstractmethod
    def request(self):
        pass


class DataBase(DataBaseInterface):
    def request(self):
        print("DataBase: conclusion data")


class ProxyDataBase(DataBaseInterface):
    def __init__(self, dataBase: DataBase):
        self._dataBase = dataBase

    def request(self):
        if self.check_access():
            self._dataBase.request()

    def check_access(self):
        print("Proxy: Checking access to data")
        return True


def client_code(dataBaseInterface: DataBaseInterface):
    dataBaseInterface.request()


if __name__ == "__main__":
    dataBase = DataBase()
    client_code(dataBase)
    proxyDataBase = ProxyDataBase(dataBase)
    client_code(proxyDataBase)