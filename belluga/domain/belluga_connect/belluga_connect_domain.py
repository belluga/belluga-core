from belluga.domain.belluga_connect.models.connection_request_model import ConnectionRequestModel
from belluga.application.common.enums.connection_request_status import ConnectionRequestStatus


class BellugaConnectDomain():

    def __init__(self, request: ConnectionRequestModel):
        self.request = request

    def counter_status_increment(self, status: ConnectionRequestStatus, increment_value: int = 1):
        print(self.request.counter)
        self.request.counter[status] = self.request.counter[status] + increment_value
        print(self.request.counter)

    def save(self):
        self.request.save()
