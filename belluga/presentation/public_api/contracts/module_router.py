from abc import ABC, abstractmethod
from fastapi_utils.inferring_router import InferringRouter

class ModuleRouter(ABC):

    @abstractmethod
    def router(self) -> InferringRouter:
        ...
        
    @abstractmethod
    def getOne(self, request_id: str):
        pass

    @abstractmethod
    def getMany(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass