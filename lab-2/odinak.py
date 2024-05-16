class Authenticator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


auth1 = Authenticator()
auth2 = Authenticator()

print(auth1 is auth2)
