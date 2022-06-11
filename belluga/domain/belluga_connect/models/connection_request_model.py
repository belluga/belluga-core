from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from belluga.application.common.enums.connection_request_status import ConnectionRequestStatus
from belluga.belluga_connection import BellugaConnection


class ConnectionRequestModel(BaseModel):
    collection: str = "connect_connection_requests"
    parent_collection: str = "connect_connections"
    id: str = None
    time: datetime = Field(...)
    payload: dict = Field(...)
    status: str = Field(...)
    connection_id: str = Field(...)
    attempts: int = Field(..., GtE=0)
    counter: dict = {
        ConnectionRequestStatus.processed: 0,
        ConnectionRequestStatus.error: 0,
        ConnectionRequestStatus.invalid: 0,
        ConnectionRequestStatus.received: 0
    }

    @staticmethod
    def helper(connection_request: dict) -> dict:
        print(connection_request)
        return ConnectionRequestModel(
            id=str(connection_request["_id"]),
            time=connection_request["time"],
            payload=dict(connection_request["payload"]),
            status=str(connection_request["status"]),
            connection_id=str(connection_request["connection_id"]),
            attempts=int(connection_request["attempts"]),
            counter=dict(connection_request.get("counter", {
                ConnectionRequestStatus.processed.value: 0,
                ConnectionRequestStatus.error.value: 0,
                ConnectionRequestStatus.invalid.value: 0,
                ConnectionRequestStatus.received.value: 0
            }))
        )

    def counter_status_increment(self, status: ConnectionRequestStatus, increment_value: int = 1):
        _set = self._counter_status_increment_build_set(
            status, increment_value)
        self._save_parent(_set)

    def _counter_status_increment_build_set(self, status: ConnectionRequestStatus, increment_value: int = 1) -> dict:
        _set = {
            "$inc": {
                "counter."+status.value: increment_value
            }
        }

        return _set

    def _build_match_id(self) -> dict:
        _match = {
            '_id': ObjectId(self.id)
        }

        return _match

    def _build_parent_match_id(self) -> dict:
        _match = {
            '_id': ObjectId(self.connection_id)
        }

        return _match

    def _save_parent(self, set: dict):
        _match = self._build_parent_match_id()
        _belluga_connection = BellugaConnection()
        _belluga_connection.connection.update(
            self.parent_collection, _match, set)
