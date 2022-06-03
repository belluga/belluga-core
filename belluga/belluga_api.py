from fastapi import FastAPI

from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaAPI():
    
    def __init__(self):
        self.api = FastAPI()
        self.connection_request = ConnectionRequestRoute()

        self.tags = ["ConnectionRequests"]
        self.prefix = "/connection_requests"

    def include_routes(self):
        self.connection_request.include_routes(self.api)