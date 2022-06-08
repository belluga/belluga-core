from abc import ABC, abstractmethod


class Singleton(ABC):

    def __init__(self, cls):
        self._cls = cls

    @abstractmethod
    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)