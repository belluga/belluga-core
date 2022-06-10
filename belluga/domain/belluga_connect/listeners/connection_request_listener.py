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

    def _on_change(self, document: dict):
        print(document)
        self.request: ConnectionRequestModel = ConnectionRequestModel.helper(document["fullDocument"])
        self.status = document["updateDescription"]["updatedFields"]["status"]

        self.connect_domain: BellugaConnectDomain = BellugaConnectDomain(self.request)
        if(self.status == "received"):
            self.connect_domain.process_received()

        if(self.status == "error"):
            self.connect_domain.process_error()

        if(self.status == "ready"):
            self.connect_domain.process_ready()

        if(self.status == "retry"):
            self.connect_domain.process_retry()

        if(self.status == "processed"):
            self.connect_domain.process_processed()