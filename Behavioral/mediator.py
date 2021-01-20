from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str):
        pass


class Alert(Mediator):
    def __init__(self, gasSensor: GasSensor, uvSensor: UVSensor):
        self._gasSensor = gasSensor
        self._gasSensor.mediator = self
        self._uvSensor = uvSensor
        self._uvSensor.mediator = self

    def notify(self, sender: object, event: str):
        if event == "modeGasA":
            print("Mediator reacts on modeGasA and triggers:")
            self._uvSensor.modeUV_A()
        elif event == "modeUV_B":
            print("Mediator reacts on modeUV_B and triggers:")
            self._gasSensor.modeGasB()
            self._uvSensor.modeUV_A()


class BaseSensor:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class GasSensor(BaseSensor):
    def modeGasA(self):
        print("GasSensor does modeGasA")
        self.mediator.notify(self, "modeGasA")

    def modeGasB(self):
        print("GasSensor does modeGasB")
        self.mediator.notify(self, "modeGasB")


class UVSensor(BaseSensor):
    def modeUV_A(self):
        print("UVSensor does modeUV_A")
        self.mediator.notify(self, "modeUV_A")

    def modeUV_B(self):
        print("UVSensor does modeUV_B")
        self.mediator.notify(self, "modeUV_B")


if __name__ == "__main__":
    gs = GasSensor()
    uvs = UVSensor()
    mediator = Alert(gs, uvs)

    print("Client triggers operation modeGasA")
    gs.modeGasA()

    print("\n", end="")

    print("Client triggers operation modeUV_B")
    uvs.modeUV_B()