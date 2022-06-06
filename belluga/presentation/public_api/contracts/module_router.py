from abc import ABC, abstractmethod, abstractproperty
from fastapi import Body, FastAPI
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from belluga.belluga_api import BellugaAPI
from belluga.belluga_connection import Belluga, BellugaConnection

from fastapi import FastAPI

class ModuleRouter(ABC):

    @abstractmethod
    def tags(self) -> list[str]:
        pass

    @abstractmethod
    def prefix(self) -> str:
        pass

    @abstractmethod
    def router(self) -> InferringRouter:
        ...

    def __init__(self):
        self.tags = ModuleRouter.tags
        self.prefix = ModuleRouter.prefix
        self.belluga_connection = BellugaConnection()
        self.belluga_api = BellugaAPI()
        self.include_routes()

    def include_routes(self):
        self.belluga_api.api.include_router(self.router, tags=self.tags,
                           prefix=self.prefix)

    @abstractmethod
    async def getOne(self, request_id: str):
        pass

    @abstractmethod
    async def getMany(self):
        pass

    @abstractmethod
    async def insert(self):
        pass

    @abstractmethod
    async def delete(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    # @abstractmethod
    # async def insert(self, connection_id: str, body: dict = Body(...)):
    #     pass