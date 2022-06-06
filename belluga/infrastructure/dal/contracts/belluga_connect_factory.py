from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.infrastructure.dal.dao.mongodb.mongodb import MongoDBDao


class BellugaConnectFactory():

    @staticmethod
    def get_client(type: str, settings: dict) -> BellugaConnect:
        print("get_client")
        print(type)
        print(settings)
        if(type == "mongodb"):
            print("will return")
            return MongoDBDao(settings["connection_string"])
        
        print("will not return")
