from fastapi import FastAPI
from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class Belluga(object):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
            return cls.instance

    def __init__(self, db_type: str, db_settings: dict):
        self.connection = BellugaConnectFactory.get_client(
            db_type, db_settings)

    def start_api(self):
        self.api = FastAPI()
        self.include_routes()

    def include_routes(self):
        self._include_route_connection_request()
    

    def _include_route_connection_request(self):
        self.connection_request = ConnectionRequestRoute()
