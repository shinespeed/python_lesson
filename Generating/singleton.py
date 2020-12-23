class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


def main():
    s = Singleton()
    print("Object created", s)
    s1 = Singleton()
    print("Object created", s1)
    s2 = Singleton()
    print("Object created", s1)
    print(s2 == s1)

if __name__ == "__main__":
    main()