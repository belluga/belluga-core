import motor.motor_asyncio as motor
from belluga.infrastructure.dal.dao.mongodb.connection_request_mongodb import ConnectionRequestMongoDB
from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.infrastructure.dal.contracts.filter_object import FilterObject


class MongoDBDao(BellugaConnect):

    def __init__(self, connection_string: str):
        self._client = motor.AsyncIOMotorClient(connection_string)
        self._database = self._client.belluga_solutions
        self._connection_request = ConnectionRequestMongoDB(self._database)

    def close(self):
        self._client.close

    async def connection_request_insert(self, connection_id: str, connection_request_data: dict) -> dict:
        return await self._connection_request.insert(connection_id, connection_request_data)
    
    async def connection_request_get(self, entity_id: str) -> list:
        _result = await self._connection_request.findOne(entity_id)
        return _result

    async def connection_request_get_many(self, filter: FilterObject) -> list:
        _result = await self._connection_request.find(filter)
        return _result

    async def watch_collection(self, collection: str, match: dict = {}):
        return self._database.get_collection(collection).watch(match)
