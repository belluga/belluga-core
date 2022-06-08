import asyncio
from threading import Thread
import time
from belluga.belluga_connection import BellugaConnection

class ConnectionRequestListener():

    _collection_str = "connect_connection_requests"

    def __init__(self, start_loop_callable):
        self.start_loop_callable = start_loop_callable
        self.update_listen()

    def update_listen(self):
        print("update_listen")
        self.update_loop = asyncio.new_event_loop()
        self.update_loop.call_soon_threadsafe(self._update_listener)
        t = Thread(target=self.start_loop_callable, args=(self.update_loop,))
        t.start()
        time.sleep(0.25)

    def _update_listener(self):
        print("_update_listener")
        _belluga_solutions = BellugaConnection()
        for document in _belluga_solutions.connection.watch_collection(self._collection_str):
            print(document)