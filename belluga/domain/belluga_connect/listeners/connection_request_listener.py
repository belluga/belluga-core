from belluga.infrastructure.dal.dao.mongodb.listener import Listener


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
        self.document = document
        self.status = document["updateDescription"]["updatedFields"]["status"]
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
        print("is received")
        # Should call domain
        print(self.document)

    def _process_error(self):
        print("is error")
        # Should call domain
        print(self.document)

    def _process_ready(self):
        print("is ready")
        # Should call domain
        print(self.document)

    def _process_retry(self):
        print("is retry")
        # Should call domain
        print(self.document)

    def _process_processed(self):
        print("is processed")
        # Should call domain
        print(self.document)
