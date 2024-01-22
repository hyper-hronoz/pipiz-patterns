class Database:
    _instance = None

    def __init__(self):
        print('Loading database')

    def __new__(cls, *args, **kwargs):
        print(cls)
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


d1 = Database()
d2 = Database()
print(d1 == d2)

