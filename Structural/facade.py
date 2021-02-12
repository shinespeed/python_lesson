from __future__ import annotations


class Computer:
    def __init__(self, cpu: CPU, mem: Memory, ssd: SSD):
        self._cpu = cpu or CPU()
        self._mem = mem or Memory()
        self._ssd = ssd or SSD()

    def operation(self):
        results = []
        results.append(self._cpu.start())
        results.append(self._mem.load())
        results.append(self._ssd.read())
        return "\n".join(results)


class CPU:
    def start(self):
        return "CPU START!"


class Memory:
    def load(self):
        return "MEMORY LOAD!"


class SSD:
    def read(self):
        return "SSD READ MEMORY"


def client_code(comp: Computer):
    print(comp.operation(), end="")


if __name__ == "__main__":
    cpu = CPU()
    ssd = SSD()
    memory = Memory()
    comp = Computer(cpu, memory, ssd)
    client_code(comp)