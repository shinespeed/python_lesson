class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, Singleton).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1)