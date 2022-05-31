from abc import ABC, abstractmethod


class Meta(ABC):

    @abstractmethod
    def parse(self, json_dream):
        pass
