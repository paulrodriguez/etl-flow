from abc import ABCMeta

class SourceInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
