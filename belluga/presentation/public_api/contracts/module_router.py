from abc import ABC, abstractmethod
from fastapi_utils.inferring_router import InferringRouter
from belluga.belluga_connection import BellugaConnection

class ModuleRouter(ABC):

    @abstractmethod
    def router(self) -> InferringRouter:
        ...

    def __init__(self):
        self.tags = ModuleRouter.tags
        self.prefix = ModuleRouter.prefix
        self.belluga_connection = BellugaConnection()

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