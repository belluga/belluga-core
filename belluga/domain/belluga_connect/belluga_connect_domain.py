from belluga.domain.belluga_connect.models.connection_request_model import ConnectionRequestModel

class BellugaConnectDomain():
    
    def __init__(self, request: ConnectionRequestModel):
        self.request = request

    def process_received(self):
        print(self.__class__)
        print("process_received")

    def process_retry(self):
        print(self.__class__)
        print("process_retry")

    def process_error(self):
        print(self.__class__)
        print("process_error")

    def process_processed(self):
        print(self.__class__)
        print("process_processed")

    def process_ready(self):
        print(self.__class__)
        print("process_ready")
    
