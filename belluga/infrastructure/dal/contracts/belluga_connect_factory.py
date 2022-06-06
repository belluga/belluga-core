from belluga.belluga_settings import BellugaSettings
from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.infrastructure.dal.dao.mongodb.mongodb import MongoDBDao


class BellugaConnectFactory():

    @staticmethod
    def get_client() -> BellugaConnect:
        _belluga_settings: BellugaSettings = BellugaSettings.instance()
        print("get_client")
        print(_belluga_settings)
        if(_belluga_settings.db_settings["type"] == "mongodb"):
            print("will return")
            return MongoDBDao(_belluga_settings.db_settings["settings"]["connection_string"])
        
        print("will not return")
