from belluga.application.common.classes.singleton import Singleton
from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory


@Singleton
class BellugaConnection(object):

    def __init__(self, db_type: str = None, db_settings: dict = None):
        print("BellugaConnect")
        print("__init__")
        print("db_type")
        print(db_type)
        print("db_settings")
        print(db_settings)
        self.connection = BellugaConnectFactory.get_client(
            db_type, db_settings)
        print(self.connection)
