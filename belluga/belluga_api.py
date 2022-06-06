from fastapi import FastAPI
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaAPI():
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
            return cls.instance

    def __init__(self):
        self.api = FastAPI()
        self.include_routes()


    def include_routes(self):
        self._include_route_connection_request()
        

    def _include_route_connection_request(self):
        self.connection_request = ConnectionRequestRoute()
        self.api.include_router(self.connection_request.router, tags=self.connection_request.tags, prefix=self.connection_request.prefix)