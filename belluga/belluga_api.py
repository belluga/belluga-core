from fastapi import FastAPI
from belluga.presentation.connect_api.routes.connection_requests import ConnectionRequestRoute


class BellugaAPI():
    
    def __new__(cls, *args, **kwargs):
        print("check instance")
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
        
        return cls.instance

    def __init__(self):
        self.api = FastAPI()