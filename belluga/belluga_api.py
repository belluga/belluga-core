from fastapi import FastAPI
from belluga.belluga_db import BellugaDB
from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory

from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaAPI():
    
    def __init__(self, belluga_db: BellugaDB):
        self.api = FastAPI()
        self.connection = BellugaConnectFactory.get_client(belluga_db)
        self.connection_request = ConnectionRequestRoute(self.connection)

    def include_routes(self):
        self.connection_request.include_routes(self.api)