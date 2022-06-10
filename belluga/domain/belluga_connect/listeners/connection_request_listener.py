from belluga.domain.belluga_connect.models.connection_request_model import ConnectionRequestModel
from belluga.infrastructure.dal.dao.mongodb.listener import Listener
from belluga.domain.belluga_connect.belluga_connect_domain import BellugaConnectDomain


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
        self.request: ConnectionRequestModel = ConnectionRequestModel.helper(self.change["fullDocument"])
        print(self.request.status)
        print(self.request.id)

    def _on_change(self, document: dict):
        self._get_data_from_change(document)

        self.connect_domain: BellugaConnectDomain = BellugaConnectDomain(self.request)
        if(self.status == "received"):
            self._process_received()

        if(self.status == "error"):
            self._process_error()

        if(self.status == "ready"):
            self._process_ready()

        if(self.status == "retry"):
            self._process_retry()

        if(self.status == "processed"):
            self._process_processed()

    def _process_received(self):
        print(self.__class__)
        print("will process the integration to get it ready")
        #TODO: Check if it's a valid request, with proper data and connection
        #TODO: Save the settings to run the integration on the document
        #TODO: Update the connection as a +1 valid
        #TODO: Update the status as 'ready'


    def _process_retry(self):
        print(self.__class__)
        print("Will just call the 'process the same way as '_process_ready'")
        #TODO: Run the integration

    def _process_error(self):
        print(self.__class__)
        print("Update CONNECTOR with a +1 error")
        #TODO: Update CONNECTOR with a +1 error
        print("We could check 'notifications rules' to see if we need to alert someone")
        #TODO: We could check "notifications rules" to see if we need to alert someone

    def _process_processed(self):
        print(self.__class__)
        print("Update CONNECTOR with a +1 success")
        #TODO: Update CONNECTOR with a +1 success
        self.connect_domain.counter_success_increment()


    def _process_ready(self):
        print(self.__class__)
        print("will run the integration")
        #TODO: Run the integration