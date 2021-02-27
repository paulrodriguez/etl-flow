from abc import ABCMeta,abstractmethod

class OperatorInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, payload, subject={}):
        """execute operator to transform the payload
        :param payload: an object with data to transform
        :param subject: dictionary with additional data
        """
        pass
