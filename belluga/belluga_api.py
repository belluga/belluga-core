from fastapi import FastAPI
from belluga.presentation.public_api.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaAPI():

    def __init__(self):
        self.api = FastAPI()
        self.include_routes()

    def include_routes(self):
        self._include_route_connection_request()

    def _include_route_connection_request(self):
        _tags = ["ConnectionRequests"]
        _prefix = "/connection_requests"
        self.connection_request = ConnectionRequestRoute()
        self.api.include_router(
            self.connection_request.router, tags=_tags, prefix=_prefix)
