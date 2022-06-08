import asyncio


class BellugaLoop(object):

    def __init__(self, loop):
        pass

    
    @staticmethod
    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
