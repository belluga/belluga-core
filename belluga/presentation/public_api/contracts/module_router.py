from abc import ABC, abstractmethod
from fastapi_utils.inferring_router import InferringRouter

class ModuleRouter(ABC):

    @abstractmethod
    def router(self) -> InferringRouter:
        ...
        
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