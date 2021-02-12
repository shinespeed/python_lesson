class Data():
    def compress(self):
        pass


class ImageFile(Data):
    def compress(self):
        return "ImageFile"


class CompressDecorator(Data):
    _data: Data = None

    def __init__(self, data: Data):
        self._data = data

    @property
    def data(self):
        return self._data

    def compress(self):
        return self._data.compress()


class GIF(CompressDecorator):

    def compress(self):
        return f"GIFCompress({self.data.compress()})"


class PNG(CompressDecorator):
    def compress(self):
        return f"PNGCompress({self.data.compress()})"


class JPEG(CompressDecorator):
    def compress(self):
        return f"JPEGCompress({self.data.compress()})"


def client_code(data: Data):
    print(f"RESULT: {data.compress()}", end="")


if __name__ == "__main__":
    simple = ImageFile()
    client_code(simple)
    print("\n")

    decorator1 = GIF(simple)
    decorator2 = JPEG(decorator1)
    client_code(decorator2)
