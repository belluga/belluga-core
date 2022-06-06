from belluga.belluga_api import BellugaAPI
from belluga.belluga_connection import BellugaConnection
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class Belluga:
    def __init__(self):
        self.api = BellugaAPI()

    def set_connection(self, db_type: str, db_settings: dict):
        self.connection = BellugaConnection(db_type, db_settings)

    def set_api(self):
        self.api = BellugaAPI()
    
    
    def include_routes(self):
        self._include_route_connection_request()
        

    def _include_route_connection_request(self):
        self.connection_request = ConnectionRequestRoute()
        ConnectionRequestRoute.include_routes(self.api)