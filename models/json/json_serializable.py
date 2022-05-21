from abc import ABC, abstractmethod


class JSONSerializable(ABC):

    @abstractmethod
    def parse(self, json_model):
        pass
