from belluga.belluga_db import BellugaDB
from belluga.infrastructure.dal.dao.mongodb.mongodb import MongoDBDao


class BellugaConnectFactory():

    @staticmethod
    def get_client(belluga_db: BellugaDB):
        if(belluga_db.type == "mongodb"):
            return MongoDBDao(belluga_db.settings["connection_string"])
