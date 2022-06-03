from fastapi import FastAPI
from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory

from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaAPI():
    
    def __init__(self, db_type: str, db_settings: dict):
        self.api = FastAPI()
        self.connection = BellugaConnectFactory.get_client(db_type, db_settings)
        self.connection_request = ConnectionRequestRoute()
        self.connection_request.set_connection(self.connection)

    def include_routes(self):
        self.connection_request.include_routes(self.api)