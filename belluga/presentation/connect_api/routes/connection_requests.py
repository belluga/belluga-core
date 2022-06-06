from datetime import datetime
from fastapi import Body, FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from belluga.infrastructure.dal.contracts.belluga_connect import BellugaConnect
from belluga.infrastructure.dal.contracts.belluga_connect_factory import BellugaConnectFactory
from belluga.presentation.public_api.contracts.module_router import ModuleRouter
from belluga.infrastructure.dal.contracts.filter_object import FilterObject
from belluga.application.common.models.response_model import ResponseModel

router = InferringRouter()
tags = ["ConnectionRequests"]
prefix = "/connection_requests"


@cbv(router)
class ConnectionRequestRoute(ModuleRouter):

    tags = tags
    prefix = prefix
    router = router

    @router.post("/{connection_id}", status_code=201, response_description="Connection Request added into the database")
    async def insert(self, connection_id: str, body: dict = Body(...)):
        new_connection_request = await self.belluga_connection.connection.connection_request_insert(connection_id, body)
        self._close()
        return ResponseModel(new_connection_request, "Connection Request added successfully.")

    @router.get("/", status_code=200, response_description="Return a list of the requests")
    async def getMany(
        self,
        status: str = None,
        since: datetime = None,
        until: datetime = None,
        connection_id: str = None,
        page: int = 1,
        items_per_page: int = 30,
    ):
        page_minimum_value = 1
        if(page < page_minimum_value):
            page = page_minimum_value

        filter = FilterObject(
            status=status,
            since=since,
            until=until,
            connection_id=connection_id,
            page=page,
            items_per_page=items_per_page
        )

        new_connection_request = await self.belluga_connection.connection.connection_request_get_many(filter)
        self._close()
        return ResponseModel(
            data=new_connection_request,
            message="Connection Request list find successfully.",
            count=len(new_connection_request),
            page=page
        )

    @router.get("/{request_id}", status_code=200, response_description="Return a specific request.")
    async def getOne(self, request_id: str):
        new_connection_request = await self.belluga_connection.connection.connection_request_get(request_id)
        self._close()
        return ResponseModel(new_connection_request, "Connection Request list find successfully.")

    async def delete(self):
        raise Exception(
            "ConnectionRequestRoute don't have 'delete' implemented")

    async def update(self):
        raise Exception(
            "ConnectionRequestRoute don't have 'update' implemented")

    def _close(self):
        self.belluga_connection.connection.close()
