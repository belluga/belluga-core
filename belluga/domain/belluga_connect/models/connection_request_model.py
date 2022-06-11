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
