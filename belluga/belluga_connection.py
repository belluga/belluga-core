from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory


class BellugaConnection(object):
    
    def __new__(cls, *args, **kwargs):
        print("check instance")
        if not hasattr(cls, "instance") or not cls.instance:
            print("__new__")
            cls.instance = super().__new__(cls)

            print(cls.instance)
            return cls.instance

    def __init__(self, db_type: str = None, db_settings: dict = None):
        print("db_type")
        print(db_type)
        print("db_settings")
        print(db_settings)
        self.connection = BellugaConnectFactory.get_client(
            db_type, db_settings)
        print(self.connection)
