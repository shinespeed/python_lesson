from typing import List


class Unit:
    def __init__(self, coord, game):
        self._coord = coord
        self._game = game

    def fire_at(self, unit, power_weapon: str, color: str, texture: str):
        self._game.add_particle(self._coord, unit._coord, power_weapon, color, texture)


class Particle:
    def __init__(self, color, sprite):
        self._color = color
        self._sprite = sprite

    def draw(self):
        print(".....Inside state.....")
        print("Adress: ", self)
        print("Color: "+ self._color)
        print("Texture: " + self._sprite)
        print("////////////////////////")


class MovingParticle:
    def __init__(self, particle: Particle, coords: str, vector: str, speed: str):
        self._particle = particle
        self._coords = coords
        self._vector = vector
        self._speed = speed

    def draw(self):
        print("////////////////////////")
        print(".....Internal state.....")
        print("Adress: ", self)
        print("Coord: " + self._coords)
        print("Vector: " + self._vector)
        print("Speed: " + self._speed)
        self._particle.draw()


class Game:
    _mps: List[MovingParticle] = []
    _particle: List[Particle] = []

    def add_particle(self, coord, vector, speed, color, sprite):
        p_temp = self.get_particle(color, sprite)
        mp_temp = MovingParticle(p_temp, coord, vector, speed)
        self._mps.append(mp_temp)

    def get_particle(self, color, sprite):
        temp_p = Particle(color, sprite)
        if len(self._particle) == 0:
            self._particle.append(temp_p)
        else:
            for particle in self._particle:
                if particle.__dict__ == temp_p.__dict__:
                    return particle
            self._particle.append(temp_p)
        return temp_p

    def draw(self):
        for mp in self._mps:
            mp.draw()


if __name__ == "__main__":
    game = Game()
    unit1 = Unit("640", game)
    unit2 = Unit("480", game)
    unit2.fire_at(unit1, "12", "red", "sprite.png")
    unit2.fire_at(unit1, "52", "red", "sprite.png")
    unit2.fire_at(unit1, "126", "blue", "sprite.png")
    unit2.fire_at(unit1, "121", "blue", "sprite.png")
    unit2.fire_at(unit1, "142", "yellow", "sprite.png")
    game.draw()