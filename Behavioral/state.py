from __future__ import annotations
from abc import ABC, abstractmethod

# Состояние — это поведенческий паттерн проектирования, который
# позволяет объектам менять поведение в зависимости от
# своего состояния. Извне создаётся впечатление, что изменился класс объекта.


class Player:
    _state = None

    def __init__(self, state: State):
        self.switch(state)

    def switch(self, state: State):
        print(f"Context: switch to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def state_play(self):
        self._state.clickPlay()

    def state_pause(self):
        self._state.clickPause()


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: Player):
        self._context = context

    @abstractmethod
    def clickPause(self):
        pass

    @abstractmethod
    def clickPlay(self):
        pass


class PlayingState(State):
    def clickPause(self):
        print("PlayingState clickPause state_pause.")
        self.context.switch(LockedState())

    def clickPlay(self):
        print("PlayingState clickPlay state_pause")


class LockedState(State):
    def clickPause(self):
        print("LockedState clickPause state_pause.")

    def clickPlay(self):
        print("LockedState clickPlay state_play.")
        self.context.switch(PlayingState())


if __name__ == "__main__":
    context = Player(PlayingState())
    context.state_pause()
    context.state_play()
