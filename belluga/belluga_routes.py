from belluga.belluga_api import BellugaAPI
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaRoutes():
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
            return cls.instance

    def __init__(self):
        self.api = BellugaAPI()
        self.include_routes()


    def include_routes(self):
        self._include_route_connection_request()
        

    def _include_route_connection_request(self):
        _tags = ["ConnectionRequests"]
        _prefix = "/connection_requests"
        self.connection_request = ConnectionRequestRoute()
        self.api.api.include_router(self.connection_request.router, tags=_tags, prefix=_prefix)