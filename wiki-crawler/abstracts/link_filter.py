from abc import ABC


class LinkFilter(ABC):
    def filter(self, link) -> bool:
        raise NotImplementedError