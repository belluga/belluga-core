from abc import ABC, abstractmethod
import asyncio
from threading import Thread
import time

from belluga.belluga_connection import BellugaConnection


class Listener(ABC):

    @property
    @abstractmethod
    def _model_class() -> str:
        pass

    @property
    @abstractmethod
    def _collection_str() -> str:
        pass

    @property
    @abstractmethod
    def _pipeline() -> list[dict]:
        pass

    def __init__(self, start_loop_callable):
        self.start_loop_callable = start_loop_callable
        self.update_listen()

    @abstractmethod
    def _on_change(self, document: dict):
        pass

    def update_listen(self):
        self.update_loop = asyncio.new_event_loop()
        self.update_loop.call_soon_threadsafe(self._update_listener)
        t = Thread(target=self.start_loop_callable, args=(self.update_loop,))
        t.start()
        time.sleep(0.25)

    def _update_listener(self):
        _belluga_solutions = BellugaConnection()
        for change in _belluga_solutions.connection.watch_collection(self._collection_str, self._pipeline):
            self._on_change(document=change)
