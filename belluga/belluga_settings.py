from belluga.application.common.classes.singleton import Singleton

class BellugaSettings(Singleton):

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def set_db(self, db_settings: dict):
        self.db_settings = db_settings