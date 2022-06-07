from datetime import datetime
from bson.objectid import ObjectId
from belluga.infrastructure.dal.entities.connection_request import ConnectionRequestsModel
from belluga.infrastructure.dal.contracts.data_object import DataObject


class ConnectionRequestMongoDB(DataObject):

    entitie_class = ConnectionRequestsModel

    def __init__(self, database):
        self.database = database
        self.connection_requests_collection = self.database.get_collection(
            "connect_connection_requests")

    def insert(self, connection_id: str, connection_request_data: dict) -> dict:
        connection_id = ObjectId(connection_id)
        connection_request: ConnectionRequestsModel = {
            "payload": connection_request_data,
            "time": datetime.utcnow(),
            "attempts": 0,
            "status": "received",
            "connection_id": connection_id
        }

        connection_request_result = self.connection_requests_collection.insert_one(connection_request)

        return {
            "connection_request_id": str(connection_request_result.inserted_id)
        }

    def findOne(self, request_id: str) -> ConnectionRequestsModel:
        match = {"_id": ObjectId(request_id)}

        _results_cursor = self.connection_requests_collection.find(match)

        _result_documents: list = []
        for document in _results_cursor:
            _request_model = ConnectionRequestsModel.helper(document)
            _result_documents.append(_request_model)

        return _request_model

    def _build_match(self) -> dict:
        def isprop(v):
            return isinstance(v, property)

        _rules = []

        for item in self.filter.items:
            k = item.name
            v = item.value

            if(v is None):
                continue

            if(k == "since"):
                _rules.append({
                    "$gte" : [
                        "$time",
                        v
                    ]
                })

            if(k == "until"):
                _rules.append({
                    "$lte" : [
                        "$time",
                        v
                    ]
                })

            if(k == "status"):
                _rules.append({
                    "$eq" : [
                        "$status",
                        v
                    ]
                })

            if(k == "connection_id"):
                _rules.append({
                    "$eq" : [
                        "$connection_id",
                        ObjectId(v)
                    ]
                })

        match = {}

        if(len(_rules) > 0):
            match = {
                "$expr" : {
                    "$and" : _rules
                }
            }

        return match

                
        
