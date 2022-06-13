from belluga.domain.belluga_connect.models.connection_request_model import ConnectionRequestModel
from belluga.infrastructure.dal.dao.mongodb.listener import Listener
from belluga.domain.belluga_connect.belluga_connect_domain import BellugaConnectDomain
from belluga.application.common.enums.connection_request_status import ConnectionRequestStatus


class ConnectionRequestListener(Listener):

    _collection_str = "connect_connection_requests"
    _pipeline = [
        {
            "$match": {
                "updateDescription.updatedFields.status": {
                    "$exists": True
                }
            }
        }
    ]

    def _get_data_from_change(self, change: dict):
        self.change = change
        self.request: ConnectionRequestModel = ConnectionRequestModel.helper(
            self.change["fullDocument"])
        print(self.request.status)
        print(self.request.id)

    def _on_change(self, document: dict):
        self._get_data_from_change(document)
        self.connect_domain: BellugaConnectDomain = BellugaConnectDomain(
            self.request)

        print(self.request.status)
        print(ConnectionRequestStatus.received)
        print(ConnectionRequestStatus.received.value)
        if(self.request.status == ConnectionRequestStatus.received.value):
            self._process_received()

        if(self.request.status == ConnectionRequestStatus.error.value):
            self._process_error()

        if(self.request.status == ConnectionRequestStatus.invalid.value):
            self._process_invalid()

        if(self.request.status == ConnectionRequestStatus.valid.value):
            self._process_valid()

        if(self.request.status == ConnectionRequestStatus.retry.value):
            self._process_retry()

        if(self.request.status == ConnectionRequestStatus.processed.value):
            self._process_processed()

    def _process_received(self):
        print(self.__class__)
        print("will process the integration to prepare and validate request")
        # TODO: Check if it's a valid request, with proper data and connection
        # TODO: Save the settings to run the integration on the document
        self.connect_domain.counter_status_increment(
            ConnectionRequestStatus.valid)
        
        self.connect_domain.status_update(
            ConnectionRequestStatus.valid)

    def _process_retry(self):
        print(self.__class__)
        print("Will just call the 'process the same way as '_process_valid'")
        # TODO: Run the integration
        self.connect_domain.run_integration()

        print("if the integreations runs correctly, then we will update to processed")
        #if the integreations runs correctly, then we will update to processed
        self.connect_domain.status_update(
            ConnectionRequestStatus.processed)

    def _process_error(self):
        self.connect_domain.counter_status_increment(
            ConnectionRequestStatus.error)

    def _process_invalid(self):
        self.connect_domain.counter_status_increment(
            ConnectionRequestStatus.invalid)

    def _process_processed(self):
        self.connect_domain.counter_status_increment(
            ConnectionRequestStatus.processed)

    def _process_valid(self):
        print(self.__class__)
        print("will run the integration")
        # TODO: Run the integration
        self.connect_domain.run_integration()

        print("if the integreations runs correctly, then we will update to processed")
        #if the integreations runs correctly, then we will update to processed
        self.connect_domain.status_update(
            ConnectionRequestStatus.processed)
