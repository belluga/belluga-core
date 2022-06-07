from abc import ABC, abstractmethod
from belluga.infrastructure.dal.contracts.filter_object import FilterObject

class DataObject(ABC):

    @property
    @abstractmethod
    def entitie_class(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    def _find(self):
        self._get_items_to_skip()
        if(self.items_to_skip == 0):
            return self.connection_requests_collection.find(self.match).limit(self.filter.items_per_page)
        
        return self.connection_requests_collection.find(self.match).limit(self.filter.items_per_page).skip(self.items_to_skip)

    def _get_items_to_skip(self) -> int:
        _page_multiplier = self.filter.page - 1
        self.items_to_skip = _page_multiplier * self.filter.items_per_page

    def find(self, filter: FilterObject):
        self.filter = filter
        self.match = self._build_match()

        _results_cursor = self._find()
        _result_documents: list = []
        for document in _results_cursor:
            _result_documents.append(self.entitie_class.helper(document))

        return _result_documents