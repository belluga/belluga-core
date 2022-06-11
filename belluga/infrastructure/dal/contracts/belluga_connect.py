from typing import Union
from abc import ABC, abstractmethod


class BellugaConnect(ABC):

    @abstractmethod
    async def connection_request_insert(self, connection_id: str, connection_request_data: dict) -> dict:
        pass

    @abstractmethod
    async def connection_request_get(self, entity_id: str) -> list:
        pass

    @abstractmethod
    async def connection_request_get_many(self, filter: Union[dict, None]) -> list:
        pass

    @abstractmethod
    def watch_collection(self, collection: str, match: dict = {}):
        pass

    @abstractmethod
    def update(self, collection: str, match: dict, set: dict):
        pass

    # @abstractmethod
    # def connection_requests_helper(self, connection_request) -> dict:
    #     pass

    @abstractmethod
    def close(self):
        pass
