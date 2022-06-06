from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory


class BellugaConnection(object):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
            return cls.instance

    def __init__(self, db_type: str, db_settings: dict):
        self.connection = BellugaConnectFactory.get_client(
            db_type, db_settings)
