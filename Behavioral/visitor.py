from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

#Посетитель — это поведенческий паттерн проектирования,
#который позволяет добавлять в программу новые операции,
#не изменяя классы объектов, над которыми эти операции могут выполняться.


class Server(ABC):
    @abstractmethod
    def accept(self, commandVisitor: CommandVisitor):
        pass


class ServerA(Server):
    def accept(self, commandVisitor: CommandVisitor):
        commandVisitor.visit_concrete_server_a(self)

    def exclusive_method_of_serverA(self):
        return "Server_A"


class ServerB(Server):
    def accept(self, commandVisitor: CommandVisitor):
        commandVisitor.visit_concrete_server_b(self)

    def special_method_of_serverB(self):
        return "Server_B"


class CommandVisitor(ABC):
    @abstractmethod
    def visit_concrete_server_a(self, server: ServerA):
        pass

    @abstractmethod
    def visit_concrete_server_b(self, server: ServerB):
        pass


class ConcretCommand(CommandVisitor):
    def visit_concrete_server_a(self, server):
        print(f"{server.exclusive_method_of_serverA()} + ConcretCommand")

    def visit_concrete_server_b(self, server):
        print(f"{server.special_method_of_serverB()} + ConcretCommand")



def client_code(servers: List[Server], commandVisitor: CommandVisitor):
    for server in servers:
        server.accept(commandVisitor)


if __name__ == "__main__":
    server_list = [ServerA(), ServerB()]

    print("The client code works with all visitors via the base Visitor interface:")
    command = ConcretCommand()
    client_code(server_list, command)
