from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory


class Belluga(object):
    
    def __new__(cls, db_type: str, db_settings: dict):
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls, db_type, db_settings)
            return cls.instance

    def __init__(self, db_type: str, db_settings: dict):
        self.connection = BellugaConnectFactory.get_client(
            db_type, db_settings)
