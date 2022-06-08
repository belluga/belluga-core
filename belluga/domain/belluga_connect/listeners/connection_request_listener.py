from ast import arg
import asyncio
from threading import Thread
import time
from belluga.belluga_connection import BellugaConnection
from belluga.infrastructure.dal.dao.mongodb.listener import Listener


class ConnectionRequestListener(Listener):

    _collection_str = "connect_connection_requests"
    _pipeline = []

    def _on_change(self, document: dict):
        print("_on_change")
        print(self.__class__)
        print(document)
        self.document = document
        if(document["operationType"] == "update"):
            self._on_update()

    def _on_update(self):
        print("is update")
        print(self.document)

    def _on_delete(self):
        print("is_delete")
        print(self.document)
        
    def _on_create(self):
        print("is_create")
        print(self.document)