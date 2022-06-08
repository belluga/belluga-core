import asyncio
from belluga.domain.belluga_connect.listeners.connection_request_listener import ConnectionRequestListener


class BellugaListener(object):

    def __init__(self):
        self.connection_request = ConnectionRequestListener(self.start_loop)
    
    # @staticmethod
    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
