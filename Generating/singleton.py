class Singleton:
    let = 'asd'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, Singleton).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    s  = Singleton()
    print(s)
    s1 = Singleton()
    print(s1)
    print(s == s1)


