from belluga.belluga_settings import BellugaSettings
from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.infrastructure.dal.dao.mongodb.mongodb import MongoDBDao


class BellugaConnectFactory():

    @staticmethod
    def get_client() -> BellugaConnect:
        _belluga_settings: BellugaSettings = BellugaSettings.instance()
        if(_belluga_settings.db_settings["type"] == "mongodb"):
            return MongoDBDao(_belluga_settings.db_settings["settings"]["connection_string"])