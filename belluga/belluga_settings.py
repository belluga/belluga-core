from belluga.application.common.classes.singleton import Singleton

class BellugaSettings():

    def set_db(self, db_settings: dict):
        self.db_settings = db_settings