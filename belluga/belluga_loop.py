from belluga.application.common.classes.singleton import Singleton
import asyncio

class BellugaLoop(Singleton):
    def __init__(self,loop):
        self.start_loop(loop)

    def instance(self, loop):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls(loop)
            return self._instance
    
    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()