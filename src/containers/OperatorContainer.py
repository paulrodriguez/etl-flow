ifrom dependency_injector import containers, providers
from ..operators.Composite import Composite

class OperatorContainer(containers.DeclarativeContainer):
    composite_factory = providers.Factory(Composite)

    @staticmethod
    def get_object():
        return OperatorContainer()
