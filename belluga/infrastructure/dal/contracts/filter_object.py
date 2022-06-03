from datetime import datetime
import inspect

from belluga.infrastructure.dal.contracts.filter_item import FilterItem


class FilterObject():

    def __init__(
        self,
        status: str = None,
        since: datetime = None,
        until: datetime = None,
        connection_id: str = None,
        page: int = 1,
        items_per_page: int = 30
        ):

        self.status = status
        self.since = since
        self.until = until
        self.connection_id = connection_id
        self.page = page
        self.items_per_page = items_per_page


        self.items: list = [
            FilterItem(name="status", value=self.status),
            FilterItem(name="since", value=self.since),
            FilterItem(name="until", value=self.until),
            FilterItem(name="connection_id", value=self.connection_id),
            FilterItem(name="page", value=self.page),
            FilterItem(name="items_per_page", value=self.items_per_page),
        ]

    # status: str = None,
    # since: datetime = None,
    # until: datetime = None,
    # connection_id: str = None
    # page: int = 1
    # items_per_page: int = 30

    # items: list = [
    #     FilterItem(name="status", value=status),
    #     FilterItem(name="since", value=since),
    #     FilterItem(name="until", value=until),
    #     FilterItem(name="connection_id", value=connection_id),
    #     FilterItem(name="page", value=page),
    #     FilterItem(name="items_per_page", value=items_per_page),
    # ]

    # _items: dict = {
    #     "status": status,
    #     "since": since,
    #     "until": until,
    #     "connection_id": connection_id,
    #     "page": page,
    #     "items_per_page": items_per_page,
    # }

    # def items(self) -> dict:
    #     return self._items.items()
