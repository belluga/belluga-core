from infrastructure.dal.dao.mongodb.mongodb import MongoDBDao


class BellugaConnectFactory():

    @staticmethod
    def get_client():
        return MongoDBDao()