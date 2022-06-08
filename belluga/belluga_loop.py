import asyncio


class BellugaLoop(object):

    def __init__(self, cls, loop):
        self._cls = cls
        self.start_loop(loop)

    def instance(self, loop):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls(loop)
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
