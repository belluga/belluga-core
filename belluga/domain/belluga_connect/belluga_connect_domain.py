from bson import ObjectId
from belluga.belluga_connection import BellugaConnection
from belluga.domain.belluga_connect.models.connection_request_model import ConnectionRequestModel
from belluga.application.common.enums.connection_request_status import ConnectionRequestStatus


class BellugaConnectDomain():

    def __init__(self, request: ConnectionRequestModel):
        self.request = request

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
            '_id': ObjectId(self.request.connection_id)
        }

        return _match

    def _save_parent(self, set: dict):
        _match = self._build_parent_match_id()
        _belluga_connection = BellugaConnection()
        _belluga_connection.connection.update(
            self.request.parent_collection, _match, set)

    def _save(self):
        pass
