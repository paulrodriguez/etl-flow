from dependency_injector import containers, providers
from ..subprocess.ImageOptimizer import ImageOptimizer

class SubprocessContainer(containers.DeclarativeContainer):
    image_optimizer_factory = providers.Factory(ImageOptimizer)

    @staticmethod
    def get_object():
        return SubprocessContainer()
