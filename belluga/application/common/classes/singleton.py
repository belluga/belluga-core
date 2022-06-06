class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def instance(self, *args, **kwargs):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls(argas=args, kwargs=kwargs)
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)