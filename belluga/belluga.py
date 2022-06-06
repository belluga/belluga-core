from django.conf import settings
from belluga.application.common.classes.singleton import Singleton
from belluga.belluga_api import BellugaAPI
from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.belluga_routes import BellugaRoutes
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute

@Singleton
class Belluga:
    
    def set_connection(self, connection: BellugaConnect):
        self.connection = connection

    def set_api(self):
        self.api = BellugaAPI.instance()
        self.routes = BellugaRoutes()