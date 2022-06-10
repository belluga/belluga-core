from datetime import datetime
from django.db import connection
from psycopg2 import connect

from pydantic import BaseModel, Field


class ConnectionRequestModel(BaseModel):
    id: str = None
    time: datetime = Field(...)
    payload: dict = Field(...)
    status: str = Field(...)
    connection_id: str = Field(...)
    attempts: int = Field(..., GtE=0)
    counter: dict = {
        "processed": 0,
        "error": 0,
        "invalid": 0,
        "received": 0
    }

    @staticmethod
    def helper(connection_request: dict) -> dict:
        return ConnectionRequestModel(
            id=str(connection_request["_id"]),
            time=connection_request["time"],
            payload=dict(connection_request["payload"]),
            status=str(connection_request["status"]),
            connection_id=str(connection_request["connection_id"]),
            attempts=int(connection_request.get["attempts", 0]),
            counter=dict(connection_request.get("counter", {
                "processed": 0,
                "error": 0,
                "invalid": 0,
                "received": 0
            }))
        )
