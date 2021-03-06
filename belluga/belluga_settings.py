from belluga.application.common.classes.singleton import Singleton

@Singleton
class BellugaSettings(object):

    def set_db(self, db_settings: dict):
        self.db_settings = db_settings