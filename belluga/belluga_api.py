from fastapi import FastAPI
from belluga.application.common.classes.singleton import Singleton
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute

@Singleton
class BellugaAPI(object):

    def __init__(self):
        self.api = FastAPI()