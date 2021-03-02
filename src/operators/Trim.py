from .OperatorInterface import OperatorInterface

class Trim(OperatorInterface):
    '''
    removes whitespace from a string.
    make sure that the values are actual strings or an error will be raised
    '''
    def __init__(self, keys=[]):
        self.keys = keys

    def execute(self, payload, subject={}):
        for key in self.keys:
            if key in payload:
                payload[key] = payload[key].strip()

        return payload
