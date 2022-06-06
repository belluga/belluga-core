from belluga.belluga_api import BellugaAPI
from belluga.belluga_connection import BellugaConnection
from belluga.belluga_routes import BellugaRoutes
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class Belluga:
    
    def set_connection(self, db_type: str, db_settings: dict):
        self.connection = BellugaConnection.instance(db_type, db_settings)

    def set_api(self):
        self.api = BellugaAPI.instance()
        self.routes = BellugaRoutes()