from fastapi import FastAPI
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute

class BellugaAPI(object):

    def __init__(self):
        self.api = FastAPI()