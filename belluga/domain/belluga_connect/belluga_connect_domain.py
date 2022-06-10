from belluga.domain.belluga_connect.models.connection_request_model import ConnectionRequestModel


class BellugaConnectDomain():

    def __init__(self, request: ConnectionRequestModel):
        self.request = request

    def counter_success_increment(self, increment_value: int = 1):
        print(self.request.counter)
        self.request.counter["success"] = self.request.counter["success"] + increment_value
        print(self.request.counter)

    def save(self):
        pass
