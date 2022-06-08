import asyncio


class BellugaLoop(object):

    def __init__(self, loop):
        self.start_loop(loop)

    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
