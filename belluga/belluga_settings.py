from belluga.application.common.classes.singleton import Singleton

class BellugaSettings(Singleton):

    def instance(self):
        return super().instance(self)

    def set_db(self, db_settings: dict):
        self.db_settings = db_settings