from belluga.application.common.classes.singleton import Singleton
import asyncio

@Singleton
class BellugaLoop:
    def __init__(self):
        self.start_loop()
    
    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()