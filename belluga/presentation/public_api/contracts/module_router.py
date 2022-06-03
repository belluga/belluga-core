from abc import ABC, abstractmethod, abstractproperty
from fastapi import Body, FastAPI
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory

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
        self.connection = BellugaConnectFactory.get_client()
        self.tags = ModuleRouter.tags
        self.prefix = ModuleRouter.prefix

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