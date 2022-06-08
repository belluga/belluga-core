from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory


class BellugaConnection(object):

    def __init__(self):
        self.connection = BellugaConnectFactory.get_client()
        self.database = self.connection
