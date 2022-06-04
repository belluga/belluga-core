from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.infrastructure.dal.dao.mongodb.mongodb import MongoDBDao


class BellugaConnectFactory():

    @staticmethod
    def get_client(type: str, settings: dict) -> BellugaConnect:
        if(type == "mongodb"):
            return MongoDBDao(settings["connection_string"])
